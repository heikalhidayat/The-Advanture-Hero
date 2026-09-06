from models.skills.magical.melee_magical import (
    ShockTounch, SlimeDivide
)

from models.skills.magical.mid_range_magical import (
    HealingGrace, HolySantuary, FrostNova, RaiseUndead
)

from models.skills.magical.long_range_magical import (
    ManaBurst, ShockWave, RepelWave, ArcaneRing, MagicShield, MagicArrow,
    SparkProjectile, Fireball, LightningStrike, MeteorStrike, GuardianLink,
    DivineIntervention, ChronoShift, GravityWell, BlackHole, Decay, SoulFeast, 
    ArmyDarkness, AcidSpit
)

from models.skills.physical.melee_physical import (
    BasicJab, LowKick, HeavyFist, HeavySmash, BattleCry, CycloneSlash,
    BerserkCharge, ShieldBash, IronFortress, GroundTremor, BastionHope, 
    SweepingLeg, PalmPush, ElbowCharge, AirSlap, StrikeSlash,
    QuickTrust, WideSwing, GuardBreak, CircularSlash, PoisonBlade, FlurryBlows,
    Assassinate, GelatinousAbsorb
)

list_skills = [
    shock_tounch := ShockTounch(),
    slime_divide := SlimeDivide(),
    healing_grace := HealingGrace(),
    holy_santuary := HolySantuary(),
    frost_nova := FrostNova(),
    raise_undead := RaiseUndead(),
    mana_burst := ManaBurst(),
    shockwave := ShockWave(),
    repel_wave := RepelWave(),
    arcane_ring := ArcaneRing(),
    magic_shield := MagicShield(),
    magic_arrow := MagicArrow(),
    spark_projectile := SparkProjectile(),
    fireball := Fireball(),
    lightning_strike := LightningStrike(),
    meteor_strike := MeteorStrike(),
    guardian_link := GuardianLink(),
    divine_intervention := DivineIntervention(),
    chrono_shift := ChronoShift(),
    gravity_well := GravityWell(),
    black_hole := BlackHole(),
    decay := Decay(),
    soul_feast := SoulFeast(),
    army_darkness := ArmyDarkness(),
    acid_spit := AcidSpit(),
    basic_jab := BasicJab(),
    low_kick := LowKick(),
    heavy_fist := HeavyFist(),
    heavy_smash := HeavySmash(),
    battle_cry := BattleCry(),
    cyclone_slash := CycloneSlash(),
    berserk_charge := BerserkCharge(),
    shield_bash := ShieldBash(),
    iron_fortress := IronFortress(),
    ground_tremor := GroundTremor(),
    bastion_hope := BastionHope(),
    sweeping_leg := SweepingLeg(),
    palm_push := PalmPush(),
    elbow_charge := ElbowCharge(),
    air_slap := AirSlap(),
    strike_slash := StrikeSlash(),
    quick_trust := QuickTrust(),
    wide_swing := WideSwing(),
    guard_break := GuardBreak(),
    circural_slash := CircularSlash(),
    poison_blade := PoisonBlade(),
    flurry_blows := FlurryBlows(),
    assassinate := Assassinate(),
    gelatinous_absorb := GelatinousAbsorb(),
]