# Spaceship Design
OOP is about modeling concepts, so this time around we are going to model spaceships for
a computer game. Follow the description below and try to implement the concepts below in
Python using the OOP principles we’ve learned so far.
Characteristics of a spaceship
- Every spaceship has a Name (string).
- Every spaceship has three combat characteristics: HP (hit points/life), Armor and Damage -
all integers.
- A ship can have 0 Armor or Damage, but all ships need to start with at least 1 HP.
- A ship with 0 HP is destroyed.
- A ship can attack another ship. This leads to a reduction of the target’s HP based on the
damage done by the source.
- A ship with no damage can’t attack.
- Armor of a ship reduces incoming damage equal to its value, but can’t reduce damage to
less than 1.
Example:
Battlecruiser: HP = 130, Damage = 15, Armor = 30
Corsair: HP = 75, Damage = 25, Armor = 8
Step 1: Battlecruiser attacks Corsair.
Damage dealt to Corsair = 15 (Battlecruiser Damage) - 8 (Corsair Armor) = 7
HP left on Corsair: 75-7 = 68
Step 2: Corsair retaliates
Damage dealt to Battlecruiser = 25 (Corsair Damage) - 30 (Battlecruiser Armor) = 1
(damage can’t be reduced to less than 1)
HP left on Battlecruiser: 129
Task
Write a program that receives the characteristics of two spaceships.
Then simulate the combat between the two spaceships:
- The two spaceships attack each other in turns. The first spaceship will always fire first.
(Extra: randomly decide at the beginning of combat which spaceship goes first)
- A spaceship that can’t attack will skip its turn. If both spaceships are in this situation the
battle ends up in a tie.
- The battle ends when one of the spaceships is destroyed.
Write each step of the simulation in the console. Include which ship attacks which at each
step, how much damage was dealt, and how much HP the target ship has left.
If a ship can’t attack, have a specific message mention this.
# EXTRA
We are going to take the game a step further. The ships can also come with upgrades
besides their main stats. They can influence either their base characteristics or add unique
effects to the combat step. All upgrades come with the ships before combat starts, and can’t
change mid-combat.
Here are some details about upgrades:
- Upgrades have a specific name associated with them.
- A ship can have as many upgrades.
- A ship can’t have the same upgrade added twice.
- You only need to cover the upgrades in the list below. (do as many as you can)
- All percent values are applied after flat values. That is, if a ship has 150 HP and we have
one upgrade grant +100 HP and another one +10% HP, the final HP value is calculated as
follows:
- Round-down all values resulting from calculations. If for example after calculation, the
armor value would come out as 2.6, the resulting armor is 2.

- Titanium Armor
Ship gets an extra +3 armor, and +250 HP.
- Absorption Shield
Ship gets an extra +50% armor.
- Proton Torpedos
Ship gets an extra 25 damage.
- Flare Engine
Ship gets +50% damage, +3 armor and +20% HP.
# [EXTRA EXTRA] EMP Cannon
Reduces the effectiveness of enemy armor by half. (armor is halved after all calculations are
done based on target’s upgrades first)
# [EXTRA EXTRA] Teleporting Module
Every incoming attack has a ¼ (25%) chance to miss. (if an attack misses it simply deals no
damage)
# [EXTRA EXTRA] Molecular Mirror
Every incoming attack has a 1/10 (10%) chance to be reflected back to the attacker. If a ship
also has the Teleporting Module, it always takes priority (if the attack is dodged it never ends
up reflected). A reflected attack cannot be reflected again, but can be dodged.
To simplify the input, you can either hardcode various ships for testing, input from a file
(adding upgrades via codes for instance), from the console, or other. Your choice!
