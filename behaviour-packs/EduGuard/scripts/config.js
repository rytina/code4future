// Aenderungen erfordern einen Server-Neustart. Keine automatische Lehrer-Ausnahme.
export const CONFIG = {
  scanTicks: 1,
  messageCooldownTicks: 60,
  cancelExplosions: true,
  emptyFilledBuckets: true,
};

export const FILLED_BUCKETS = new Set([
  "water_bucket", "lava_bucket", "powder_snow_bucket", "axolotl_bucket",
  "cod_bucket", "salmon_bucket", "pufferfish_bucket", "tropical_fish_bucket", "tadpole_bucket",
].map(id => `minecraft:${id}`));

export const BANNED_ITEMS = new Set([
  ...FILLED_BUCKETS,
  ...[
    "ender_pearl", "chorus_fruit", "tnt", "tnt_minecart", "end_crystal",
    "flint_and_steel", "fire_charge", "respawn_anchor",
    "water", "flowing_water", "lava", "flowing_lava",
    "command_block", "chain_command_block", "repeating_command_block",
    "command_block_minecart", "structure_block", "structure_void", "allow", "deny",
    "border_block", "jigsaw", "lava_cauldron", "water_cauldron",
  ].map(id => `minecraft:${id}`),
]);

export function isBanned(id) {
  return !!id && BANNED_ITEMS.has(id);
}

export const BLOCKED_INTERACTIONS = new Set([
  "minecraft:respawn_anchor",
  "minecraft:command_block", "minecraft:chain_command_block",
  "minecraft:repeating_command_block", "minecraft:structure_block",
]);
