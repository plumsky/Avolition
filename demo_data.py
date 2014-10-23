﻿items={
        "potion":{'model':"models/flask",
                  'scale':0.15,
                  'gui':"icon/icon_flask.png",
                  'command':"heal"},
        "key":{'model':"models/key",
                  'scale':0.08,
                  'gui':"icon/icon_key2.png",
                  'command':"key_pickup"},
        "exit":{'model':"models/empty",
                  'scale':1,
                  'gui':"icon/icon_lock1.png",
                  'command':"exit"},            
      }

levels=[               
       
       {"map_name":"models/level2.bam",      
       "map_monsters":[10, 11, 12,16],
       "num_monsters":3,
       "kills_for_key":15,
       "enter":[-3,0,0],
       "exit":[54.5,-11,0]},
       
       {"map_name":"models/level_a3.bam",      
       "map_monsters":[2,3,3,4,4],
       "num_monsters":4,
       "kills_for_key":25,
       "enter":[0,1,0],
       "exit":[30,43,0]},
       
       {"map_name":"models/end_level.bam",      
       "map_monsters":[0],
       "num_monsters":0,
       "kills_for_key":20,
       "enter":[0.0,0.0,0],
       "exit":[100,100,0]},
       ]

monster_names={"goblin":0,
               "metal_golem":1,
               "gold_golem":2,
               "lava_golem1":3,
               "lava_golem2":4,
               "magic_golem":5,
               "rock_golem1":6,
               "rock_golem2":7,
               "paskuda":8,
               "lagun_monster":9,
               "zombie_sick":10,
               "zombie_brain":11,
               "zombie_wound":12,
               "zombie_dry":13,
               "zombie_sick2":14,
               "zombie_noarm":15,
               "skeleton":16,}
monsters=[
        {
        "model":"models/npc/m_goblin",
        "root_bone":"Bip01 Spine2",
        "anim":{"walk":"models/npc/a_goblin_walk","attack":"models/npc/a_goblin_attack","die":"models/npc/a_goblin_die"},
        "speed":1.0,
        "scale":0.09,
        "heading":0,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die7',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":90,
        "armor":0,
        "dmg":5        
        },
        {
        "model":"models/npc/m_golem_metal",
        "root_bone":"body",
        "anim":{"walk":"models/npc/a_golem1_walk","attack":"models/npc/a_golem1_attack","die":"models/npc/a_golem1_die"},
        "speed":2.2,
        "scale":0.14,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit_metal',
        "die_sfx":'die_metal',
        "arrowhit_sfx":'hit_arrow_metal',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3,.4,.2],
        "hp":130,
        "armor":5,
        "dmg":3
        },
        {
        "model":"models/npc/m_golem_gold",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":1.35,
        "scale":0.38,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit3',
        "die_sfx":'die4',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":100,
        "armor":2,
        "dmg":6
        },
        {
        "model":"models/npc/m_golem_lava1",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":1.2,
        "scale":0.38,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die3',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":150,
        "armor":3,
        "dmg":8
        },
        {
        "model":"models/npc/m_golem_lava2",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":.95,
        "scale":0.39,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die1',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":140,
        "armor":1,
        "dmg":7
        },
        {
        "model":"models/npc/m_golem_magic",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":1.1,
        "scale":0.38,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die6',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":175,
        "armor":5,
        "dmg":9
        },
        {
        "model":"models/npc/m_golem_rock1",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":1.0,
        "scale":0.38,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die3',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":120,
        "armor":2,
        "dmg":10
        },
        {
        "model":"models/npc/m_golem_rock2",
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_golem2_walk","attack":"models/npc/a_golem2_attack","die":"models/npc/a_golem2_die"},
        "speed":0.95,
        "scale":0.39,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die3',
        "arrowhit_sfx":'hit_arrow_rock',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.3],
        "hp":130,
        "armor":3,
        "dmg":8
        },
        {
        "model":"models/npc/m_monster1",        
        "root_bone":"Bip001 Spine",
        "anim":{"walk":"models/npc/a_monster1_walk","attack":"models/npc/a_monster1_attack","die":"models/npc/a_monster1_die"},
        "speed":1.0,
        "scale":0.24,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die5',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[1.0, .3],
        "hp":100,
        "armor":0,
        "dmg":4
        },
        {
        "model":"models/npc/m_monster2",              
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_monster2_walk","attack":"models/npc/a_monster2_attack","die":"models/npc/a_monster2_die"},
        "speed":1.1,
        "scale":0.27,
        "heading":180,
        "hit_vfx":'vfx/blood_green.png',
        "hit_sfx":'hit1',
        "die_sfx":'die6',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.5],
        "hp":200,
        "armor":0,
        "dmg":11
        },
        {
        "model":"models/npc/m_zombie1",           
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk1","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.0,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die1',        
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":50,
        "armor":0,
        "dmg":5
        },
        {
        "model":"models/npc/m_zombie2",        
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk1","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.0,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die1',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":60,
        "armor":0,
        "dmg":6
        },
        {
        "model":"models/npc/m_zombie3",        
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk2","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.1,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die1',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":70,
        "armor":0,
        "dmg":7
        },
        {
        "model":"models/npc/m_zombie4",        
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk3","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.0,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die1',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":80,
        "armor":0,
        "dmg":7
        },
        {
        "model":"models/npc/m_zombie5",        
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk2","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.0,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die2',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":90,
        "armor":0,
        "dmg":8
        },
        {
        "model":"models/npc/m_zombie6",        
        "root_bone":"Bip001 Spine1",
        "anim":{"walk":"models/npc/a_zombie_walk3","attack":"models/npc/a_zombie_attack","die":"models/npc/a_zombie_die"},
        "speed":1.0,
        "scale":0.024,
        "heading":180,
        "hit_vfx":'vfx/blood_red.png',
        "hit_sfx":'hit2',
        "die_sfx":'die2',
        "arrowhit_sfx":'hit_arrow',
        "attack_sfx":'m_attack1',
        "attack_pattern":[.4],
        "hp":100,
        "armor":0,
        "dmg":9
        },
        {
        "model":"models/npc/m_skel",        
        "root_bone":"Bip001 Spine2",
        "anim":{"walk":"models/npc/a_skel_walk","attack":"models/npc/a_skel_attack","die":"models/npc/a_skel_die"},
        "speed":1.0,
        "scale":0.1,
        "heading":180,
        "hit_vfx":'vfx/sparks.png',
        "hit_sfx":'hit1',
        "die_sfx":'die6',
        "arrowhit_sfx":'hit_arrow_bone',
        "attack_sfx":'m_attack1',
        "attack_pattern":[5.2, .5],
        "hp":110,
        "armor":2,
        "dmg":5
        }
      ]
