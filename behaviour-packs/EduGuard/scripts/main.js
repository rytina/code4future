import { world, system, ItemStack, EquipmentSlot, PlayerPermissionLevel } from "@minecraft/server";
import { CONFIG, FILLED_BUCKETS, isBanned, BLOCKED_INTERACTIONS } from "./config.js";

function isOperator(player) {
  return player.playerPermissionLevel === PlayerPermissionLevel.Operator;
}

const lastMessage = new Map();
const pending = new Set();
let lastError = -1200;

function report(error) {
  if (system.currentTick - lastError >= 1200) {
    lastError = system.currentTick;
    console.error(`[EduGuard] Laufzeitfehler: ${error}`);
  }
}

function notify(player) {
  if (isOperator(player)) return;
  const now = system.currentTick;
  if (now - (lastMessage.get(player.id) ?? -10000) < CONFIG.messageCooldownTicks) return;
  lastMessage.set(player.id, now);
  player.sendMessage("§c[EduGuard] Dieser Gegenstand oder diese Aktion ist auf dem Schulserver gesperrt.");
}

function replacement(item) {
  if (CONFIG.emptyFilledBuckets && FILLED_BUCKETS.has(item.typeId)) {
    return new ItemStack("minecraft:bucket", item.amount);
  }
  return undefined;
}

// Immer den aktuellen Slotinhalt lesen: Ein Slotwechsel darf kein anderes Item loeschen.
function sanitize(player) {
  if (isOperator(player)) return;
  const inventory = player.getComponent("minecraft:inventory")?.container;
  let changed = false;
  if (inventory) {
    for (let slot = 0; slot < inventory.size; slot++) {
      const item = inventory.getItem(slot);
      if (item && isBanned(item.typeId)) {
        inventory.setItem(slot, replacement(item));
        changed = true;
      }
    }
  }
  const equipment = player.getComponent("minecraft:equippable");
  const offhand = equipment?.getEquipment(EquipmentSlot.Offhand);
  if (offhand && isBanned(offhand.typeId)) {
    equipment.setEquipment(EquipmentSlot.Offhand, replacement(offhand));
    changed = true;
  }
  if (changed) notify(player);
}

function deny(event, player) {
  if (isOperator(player)) return;
  event.cancel = true; // Unmittelbar im Before-Event, niemals erst in system.run.
  if (pending.has(player.id)) return;
  pending.add(player.id);
  const id = player.id;
  system.run(() => {
    pending.delete(id);
    try { sanitize(player); notify(player); } catch (error) { report(error); }
  });
}

// Kein stiller Rueckfall auf blosses Inventar-Polling bei fehlender API.
for (const name of ["itemUse", "playerInteractWithBlock", "playerInteractWithEntity", "playerBreakBlock", "explosion"]) {
  if (!world.beforeEvents[name]?.subscribe) {
    throw new Error(`[EduGuard] NICHT AKTIV: erforderliches Before-Event fehlt: ${name}`);
  }
}

world.beforeEvents.itemUse.subscribe(event => {
  if (isBanned(event.itemStack?.typeId)) deny(event, event.source);
});
world.beforeEvents.playerInteractWithBlock.subscribe(event => {
  const blockId = event.block.typeId;
  const unsafeBed = blockId === "minecraft:bed" && event.player.dimension.id !== "minecraft:overworld";
  if (isBanned(event.itemStack?.typeId) || BLOCKED_INTERACTIONS.has(blockId) || unsafeBed) {
    deny(event, event.player);
  }
});
world.beforeEvents.playerInteractWithEntity.subscribe(event => {
  if (isBanned(event.itemStack?.typeId)) deny(event, event.player);
});
world.beforeEvents.playerBreakBlock.subscribe(event => {
  if (["minecraft:ice", "minecraft:frosted_ice"].includes(event.block.typeId)) deny(event, event.player);
});
world.beforeEvents.explosion.subscribe(event => {
  if (CONFIG.cancelExplosions) event.cancel = true;
});
world.afterEvents.playerSpawn.subscribe(event => {
  try {
    sanitize(event.player);
    if (event.initialSpawn) event.player.sendMessage("§a[EduGuard] Schutzskript geladen (1.0.0).");
  } catch (error) { report(error); }
});
world.afterEvents.playerLeave.subscribe(event => {
  lastMessage.delete(event.playerId);
  pending.delete(event.playerId);
});
system.runInterval(() => {
  for (const player of world.getAllPlayers()) {
    try { sanitize(player); } catch (error) { report(error); }
  }
}, CONFIG.scanTicks);
system.run(() => console.warn("[EduGuard] AKTIV 1.0.0 – Before-Handler registriert. Abnahmetest erforderlich."));
