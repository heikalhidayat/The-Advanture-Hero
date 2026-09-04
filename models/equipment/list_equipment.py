from models.equipment.strength_equipment import (
    GreatSword, BattleAxe, LongSword, Mace, IronGauntlets
)
from models.equipment.agility_equipment import (
    Dagger, LeatherBoots, ClothCloak, SilverNecklace, PocketWatch
)
from models.equipment.defense_equipment import (
    IronShield, ChainMail, IronHelm
)
from models.equipment.magic_equipment import (
    WoodenStaff, MagicWand, SilkRobe, MageHat, CrystalRing
)
from models.equipment.dexterity_equipment import (
    ShortBow, LeatherGloves, LeatherHood
)
from models.equipment.resistance_equipment import (
    HeavyCloak, LeatherVest, JadeRing, Talisman
)

list_equipment = [
    great_sword := GreatSword(),
    battle_axe := BattleAxe(),
    long_sword := LongSword(),
    mace := Mace(),
    short_bow := ShortBow(),
    iron_gauntlet := IronGauntlets(),
    dagger := Dagger(),
    leather_boots := LeatherBoots(),
    cloth_cloak := ClothCloak(),
    silver_necklace := SilverNecklace(),
    pocket_watch := PocketWatch(),
    iron_shield := IronShield(),
    chain_mail := ChainMail(),
    iron_helm := IronHelm(),
    wooden_staff := WoodenStaff(),
    magic_wand := MagicWand(),
    silk_robe := SilkRobe(),
    mage_hat := MageHat(),
    crystal_ring := CrystalRing(),
    short_bow := ShortBow(),
    leather_gloves := LeatherGloves(),
    leather_hood := LeatherHood(),
    heavy_cloak := HeavyCloak(),
    leather_vest := LeatherVest(),
    jade_ring := JadeRing(),
    talisman := Talisman()
]