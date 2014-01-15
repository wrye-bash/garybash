# -*- coding: utf-8 -*-

# Wrye Flash
# Module for Fallout 3 definitions.
# When Flash decides what game it should run for, it should then import this module as
# import fallout3 as game
# All code changes made during the merge reference this game module alias instead of a specific game.

#--The main plugin Wrye Bash should look for
masterFiles = [
    u'Fallout3.esm',
    ]
    
#--Script Extender information
class se:
    shortName = u'FOSE'                      # Abbreviated name
    longName = u'Fallout 3 Script Extender'   # Full name
    exe = u'fose_loader.exe'                 # Exe to run
    steamExe = u'fose_loader.dll'           # Exe to run if a steam install
    url = u'http://fose.silverlock.org/'     # URL to download from
    urlTip = u'http://fose.silverlock.org/'  # Tooltip for mouse over the URL
    
#--Game ESM/ESP/BSA files
bethDataFiles = set((
    #--Vanilla
    r'fallout3.esm',
    r'fallout - menuvoices.bsa',
    r'fallout - meshes.bsa',
    r'fallout - misc.bsa',
    r'fallout - sound.bsa',
    r'fallout - textures.bsa',
    r'fallout - voices.bsa',
    #-- DLC
    r'anchorage.esm',
    r'anchorage - main.bsa',
    r'anchorage - sounds.bsa',
    r'thepitt.esm',
    r'thepitt - main.bsa',
    r'thepitt - sounds.bsa',
    r'brokensteel.esm',
    r'brokensteel - main.bsa',
    r'brokensteel - sounds.bsa',
    r'pointlookout.esm',
    r'pointlookout - main.bsa',
    r'pointlookout - sounds.bsa',
    r'zeta.esm',
    r'zeta - main.bsa',
    r'zeta - sounds.bsa',
    ))
allBethFiles = set((
    #vanilla
    r'Credits.txt',
    r'CreditsWacky.txt',
    r'Fallout3.esm',
    r'Fallout - MenuVoices.bsa',
    r'Fallout - Meshes.bsa',
    r'Fallout - Misc.bsa',
    r'Fallout - Sound.bsa',
    r'Fallout - Textures.bsa',
    r'Fallout - Voices.bsa',
    r'LODSettings\aaaForgotten1.DLODSettings',
    r'LODSettings\aaaForgotten4.DLODSettings',
    r'LODSettings\aaaForgotten5.DLODSettings',
    r'Music\Base\Base_01.mp3',
    r'Music\Base\Base_02.mp3',
    r'Music\Base\Base_03.mp3',
    r'Music\Base\Base_04.mp3',
    r'Music\Battle\Battle_01.mp3',
    r'Music\Battle\Battle_02.mp3',
    r'Music\Battle\Battle_03.mp3',
    r'Music\Battle\Battle_04.mp3',
    r'Music\Battle\Battle_05.mp3',
    r'Music\Battle\Battle_06.mp3',
    r'Music\Battle\Battle_07.mp3',
    r'Music\Battle\Finale\Battle_01.mp3',
    r'Music\Battle\Finale\Battle_02.mp3',
    r'Music\Battle\Finale\Battle_03.mp3',
    r'Music\Battle\Finale\Battle_04.mp3',
    r'Music\Battle\Finale\Battle_05.mp3',
    r'Music\Battle\Finale\Battle_06.mp3',
    r'Music\Battle\Finale\Battle_07.mp3',
    r'Music\Dungeon\Dungeon_01.mp3',
    r'Music\Dungeon\Dungeon_02.mp3',
    r'Music\Dungeon\Dungeon_03.mp3',
    r'Music\Dungeon\Dungeon_04.mp3',
    r'Music\Dungeon\Dungeon_05.mp3',
    r'Music\Endgame\Endgame_01.mp3',
    r'Music\Endgame\Endgame_02.mp3',
    r'Music\Endgame\Endgame_03.mp3',
    r'Music\Endgame\Endgame_04.mp3',
    r'Music\Endgame\Endgame_05.mp3',
    r'Music\Endgame\Endgame_06.mp3',
    r'Music\Endgame\Endgame_07.mp3',
    r'Music\Endgame\Endgame_08.mp3',
    r'Music\Endgame\Endgame_09.mp3',
    r'Music\Endgame\Endgame_11.mp3',
    r'Music\Endgame\Endgame_12.mp3',
    r'Music\Endgame\Endgame_14.mp3',
    r'Music\Endgame\Endgame_15.mp3',
    r'Music\Endgame\Endgame_17.mp3',
    r'Music\Endgame\Endgame_18.mp3',
    r'Music\Endgame\Endgame_19.mp3',
    r'Music\Explore\Explore_01.mp3',
    r'Music\Explore\Explore_02.mp3',
    r'Music\Explore\Explore_03.mp3',
    r'Music\Explore\Explore_04.mp3',
    r'Music\Explore\Explore_05.mp3',
    r'Music\Explore\Explore_06.mp3',
    r'Music\Explore\Explore_07.mp3',
    r'Music\Public\Public_01.mp3',
    r'Music\Public\Public_02.mp3',
    r'Music\Public\Public_03.mp3',
    r'Music\Public\Public_04.mp3',
    r'Music\Public\Public_05.mp3',
    r'Music\Special\Death.mp3',
    r'Music\Special\ExitTheVault.mp3',
    r'Music\Special\MainTitle.mp3',
    r'Music\Special\Success.mp3',
    r'Music\Tension\Tension_01.mp3',
    r'Music\TranquilityLane\MUS_TranquilityLane_01_LP.mp3',
    r'Music\TranquilityLane\MUS_TranquilityLane_02_LP.mp3',
    r'Shaders\shaderpackage002.sdp',
    r'Shaders\shaderpackage003.sdp',
    r'Shaders\shaderpackage004.sdp',
    r'Shaders\shaderpackage006.sdp',
    r'Shaders\shaderpackage007.sdp',
    r'Shaders\shaderpackage009.sdp',
    r'Shaders\shaderpackage010.sdp',
    r'Shaders\shaderpackage011.sdp',
    r'Shaders\shaderpackage012.sdp',
    r'Shaders\shaderpackage013.sdp',
    r'Shaders\shaderpackage014.sdp',
    r'Shaders\shaderpackage015.sdp',
    r'Shaders\shaderpackage016.sdp',
    r'Shaders\shaderpackage017.sdp',
    r'Shaders\shaderpackage018.sdp',
    r'Shaders\shaderpackage019.sdp',
    r'Video\1 year later.bik',
    r'Video\2 weeks later.bik',
    r'Video\3 years later.bik',
    r'Video\6 years later.bik',
    r'Video\9 years later.bik',
    r'Video\B01.bik',
    r'Video\B02.bik',
    r'Video\B03.bik',
    r'Video\B04.bik',
    r'Video\B05.bik',
    r'Video\B06.bik',
    r'Video\B07.bik',
    r'Video\B08.bik',
    r'Video\B09.bik',
    r'Video\B10.bik',
    r'Video\B11.bik',
    r'Video\B12.bik',
    r'Video\B13.bik',
    r'Video\B14.bik',
    r'Video\B15.bik',
    r'Video\B16.bik',
    r'Video\B17.bik',
    r'Video\B18.bik',
    r'Video\B19.bik',
    r'Video\B20.bik',
    r'Video\B21.bik',
    r'Video\B22.bik',
    r'Video\B23.bik',
    r'Video\B24.bik',
    r'Video\B25.bik',
    r'Video\B26.bik',
    r'Video\B27.bik',
    r'Video\B28.bik',
    r'Video\B29.bik',
    r'Video\Fallout INTRO Vsk.bik',
    #DLCs
    r'anchorage.esm',
    r'anchorage - main.bsa',
    r'anchorage - sounds.bsa',
    r'thepitt.esm',
    r'thepitt - main.bsa',
    r'thepitt - sounds.bsa',
    r'brokensteel.esm',
    r'brokensteel - main.bsa',
    r'brokensteel - sounds.bsa',
    r'pointlookout.esm',
    r'pointlookout - main.bsa',
    r'pointlookout - sounds.bsa',
    r'zeta.esm',
    r'zeta - main.bsa',
    r'zeta - sounds.bsa',
    r'DLCList.txt',
    ))
    
# Installer -------------------------------------------------------------------
# ensure all path strings are prefixed with 'r' to avoid interpretation of
# accidental escape sequences
ignoreDataFiles = set((
#    r'FOSE\Plugins\Construction Set Extender.dll',
#    r'FOSE\Plugins\Construction Set Extender.ini'
    ))
ignoreDataDirs = set((
#    r'FOSE\Plugins\ComponentDLLs\CSE',
    r'LSData'
    ))
    
# Tes3 Group/Top Types -------------------------------------------------------------

#--Top types in Fallout3 order.
topTypes = ['GMST', 'TXST', 'MICN', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'HAIR', 'EYES',
    'RACE', 'SOUN', 'ASPC', 'MGEF', 'SCPT', 'LTEX', 'ENCH', 'SPEL', 'ACTI', 'TACT',
    'TERM', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'STAT', 'SCOL',
    'MSTT', 'PWAT', 'GRAS', 'TREE', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'CREA', 'LVLC',
    'LVLN', 'KEYM', 'ALCH', 'IDLM', 'NOTE', 'COBJ', 'PROJ', 'LVLI', 'WTHR', 'CLMT',
    'REGN', 'NAVI', 'CELL', 'WRLD', 'DIAL', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR',
    'ANIO', 'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD',
    'ADDN', 'AVIF', 'RADS', 'CAMS', 'CPTH', 'VTYP', 'IPCT', 'IPDS', 'ARMA', 'ECZN',
    'MESG', 'RGDL', 'DOBJ', 'LGTM', 'MUSC',
    # Unused types in fallout3. (dummy)
    'SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA',
    ]
    
# Added topTypes are...
# ['BPTD', 'VTYP', 'MUSC', 'FLST', 'PWAT', 'MICN', 'AVIF', 'NOTE', 'TERM', 'ASPC',
#  'PERK', 'HDPT', 'TXST', 'DOBJ', 'NAVI', 'EXPL', 'IPDS', 'IDLM', 'ARMA', 'LVLN',
#  'MSTT', 'IMAD', 'TACT', 'RGDL', 'CPTH', 'IMGS', 'MESG', 'DEBR', 'LGTM', 'SCOL',
#  'ECZN', 'CAMS', 'RADS', 'PROJ', 'IPCT', 'ADDN', 'COBJ']
#
# Removed topTypes are...
# ['SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA']

# Id Functions ----------------------------------------------------------------

ob = getIdFunc('fallout3.esm')


# Function Info ---------------------------------------------------------------
conditionFunctionData = ( #--0: no param; 1: int param; 2: formid param
    (153, 'CanHaveFlames', 0, 0, 0, 0),
    (127, 'HasBeenEatan', 0, 0, 0, 0),
    ( 14, 'GetActorValue', 1, 0, 0, 0),
    ( 61, 'GetAlarmed', 0, 0, 0, 0),
    (190, 'GetAmountSoldStolen', 0, 0, 0, 0),
    (  8, 'GetAngle', 1, 0, 0, 0),
    ( 81, 'GetArmorRating', 0, 0, 0, 0),
    (274, 'GetArmorRatingUpperBody', 0, 0, 0, 0),
    ( 63, 'GetAttacked', 0, 0, 0, 0),
    (264, 'GetBarterGold', 0, 0, 0, 0),
    (277, 'GetBaseActorValue', 1, 0, 0, 0),
    (229, 'GetClassDefaultMatch', 0, 0, 0, 0),
    ( 41, 'GetClothingValue', 0, 0, 0, 0),
    (122, 'GetCrime', 2, 1, 0, 0),
    (116, 'GetMinorCrimeCount', 0, 0, 0, 0),
    (110, 'GetCurrentAIPackage', 0, 0, 0, 0),
    (143, 'GetCurrentAIProcedure', 0, 0, 0, 0),
    ( 18, 'GetCurrentTime', 0, 0, 0, 0),
    (148, 'GetCurrentWeatherPercent', 0, 0, 0, 0),
    (170, 'GetDayOfWeek', 0, 0, 0, 0),
    ( 46, 'GetDead', 0, 0, 0, 0),
    ( 84, 'GetDeadCount', 2, 0, 0, 0),
    (203, 'GetDestroyed', 0, 0, 0, 0),
    ( 45, 'GetDetected', 2, 0, 0, 0),
    (180, 'GetDetectionLevel', 2, 0, 0, 0),
    ( 35, 'GetDisabled', 0, 0, 0, 0),
    ( 39, 'GetDisease', 0, 0, 0, 0),
    ( 76, 'GetDisposition', 2, 0, 0, 0),
    (  1, 'GetDistance', 2, 0, 0, 0),
    (215, 'GetDefaultOpen', 0, 0, 0, 0),
    (182, 'GetEquipped', 2, 0, 0, 0),
    ( 73, 'GetFactionRank', 2, 0, 0, 0),
    ( 60, 'GetFactionRankDifference', 2, 2, 0, 0),
    (128, 'GetFatiguePercentage', 0, 0, 0, 0),
    (288, 'GetFriendHit', 2, 0, 0, 0),
    (160, 'GetFurnitureMarkerID', 0, 0, 0, 0),
    ( 74, 'GetGlobalValue', 2, 0, 0, 0),
    ( 48, 'GetGold', 0, 0, 0, 0),
    ( 99, 'GetHeadingAngle', 2, 0, 0, 0),
    (318, 'GetIdleDoneOnce', 0, 0, 0, 0),
    (338, 'GetIgnoreFriendlyHits', 0, 0, 0, 0),
    ( 67, 'GetInCell', 2, 0, 0, 0),
    (230, 'GetInCellParam', 2, 2, 0, 0),
    ( 71, 'GetInFaction', 2, 0, 0, 0),
    ( 32, 'GetInSameCell', 2, 0, 0, 0),
    (310, 'GetInWorldspace', 2, 0, 0, 0),
    ( 91, 'GetIsAlerted', 0, 0, 0, 0),
    ( 68, 'GetIsClass', 2, 0, 0, 0),
    (228, 'GetIsClassDefault', 2, 0, 0, 0),
    ( 64, 'GetIsCreature', 0, 0, 0, 0),
    (161, 'GetIsCurrentPackage', 2, 0, 0, 0),
    (149, 'GetIsCurrentWeather', 2, 0, 0, 0),
    (237, 'GetIsGhost', 0, 0, 0, 0),
    ( 72, 'GetIsID', 2, 0, 0, 0),
    (254, 'GetIsPlayableRace', 0, 0, 0, 0),
    (224, 'GetVATSMode', 0, 0, 0, 0),
    ( 69, 'GetIsRace', 2, 0, 0, 0),
    (136, 'GetIsReference', 2, 0, 0, 0),
    ( 70, 'GetIsSex', 1, 0, 0, 0),
    (246, 'GetIsUsedItem', 2, 0, 0, 0),
    (247, 'GetIsUsedItemType', 1, 0, 0, 0),
    ( 47, 'GetItemCount', 2, 0, 0, 0),
    (107, 'GetKnockedState', 0, 0, 0, 0),
    ( 80, 'GetLevel', 0, 0, 0, 0),
    ( 27, 'GetLineOfSight', 2, 0, 0, 0),
    (  5, 'GetLocked', 0, 0, 0, 0),
    ( 65, 'GetLockLevel', 0, 0, 0, 0),
    (320, 'GetNoRumors', 0, 0, 0, 0),
    (255, 'GetOffersServicesNow', 0, 0, 0, 0),
    (157, 'GetOpenState', 0, 0, 0, 0),
    (193, 'GetPCExpelled', 2, 0, 0, 0),
    (199, 'GetPCFactionAttack', 2, 0, 0, 0),
    (195, 'GetPCFactionMurder', 2, 0, 0, 0),
    (197, 'GetPCEnemyofFaction', 2, 0, 0, 0),
    (132, 'GetPCInFaction', 2, 0, 0, 0),
    (129, 'GetPCIsClass', 2, 0, 0, 0),
    (130, 'GetPCIsRace', 2, 0, 0, 0),
    (131, 'GetPCIsSex', 1, 0, 0, 0),
    (312, 'GetPCMiscStat', 1, 0, 0, 0),
    (225, 'GetPersuasionNumber', 0, 0, 0, 0),
    ( 98, 'GetPlayerControlsDisabled', 0, 0, 0, 0),
    (365, 'IsChild', 0, 0, 0, 0),
    (362, 'GetPlayerHasLastRiddenHorse', 0, 0, 0, 0),
    (  6, 'GetPos', 1, 0, 0, 0),
    ( 56, 'GetQuestRunning', 2, 0, 0, 0),
    ( 79, 'GetQuestVariable', 2, 1, 0, 0),
    ( 77, 'GetRandomPercent', 0, 0, 0, 0),
    (244, 'GetRestrained', 0, 0, 0, 0),
    ( 24, 'GetScale', 0, 0, 0, 0),
    ( 53, 'GetScriptVariable', 2, 1, 0, 0),
    ( 12, 'GetSecondsPassed', 0, 0, 0, 0),
    ( 66, 'GetShouldAttack', 2, 0, 0, 0),
    (159, 'GetSitting', 0, 0, 0, 0),
    ( 49, 'GetSleeping', 0, 0, 0, 0),
    ( 58, 'GetStage', 2, 0, 0, 0),
    ( 59, 'GetStageDone', 2, 1, 0, 0),
    ( 11, 'GetStartingAngle', 1, 0, 0, 0),
    ( 10, 'GetStartingPos', 1, 0, 0, 0),
    ( 50, 'GetTalkedToPC', 0, 0, 0, 0),
    (172, 'GetTalkedToPCParam', 2, 0, 0, 0),
    (361, 'GetTimeDead', 0, 0, 0, 0),
    (315, 'GetTotalPersuasionNumber', 0, 0, 0, 0),
    (144, 'GetTrespassWarningLevel', 0, 0, 0, 0),
    (242, 'GetUnconscious', 0, 0, 0, 0),
    (259, 'GetUsedItemActivate', 0, 0, 0, 0),
    (258, 'GetUsedItemLevel', 0, 0, 0, 0),
    ( 40, 'GetVampire', 0, 0, 0, 0),
    (142, 'GetWalkSpeed', 0, 0, 0, 0),
    (108, 'GetWeaponAnimType', 0, 0, 0, 0),
    (109, 'IsWeaponSkillType', 1, 0, 0, 0),
    (147, 'GetWindSpeed', 0, 0, 0, 0),
    (154, 'HasFlames', 0, 0, 0, 0),
    (214, 'HasMagicEffect', 2, 0, 0, 0),
    (227, 'HasCannibal', 0, 0, 0, 0),
    (353, 'IsActor', 0, 0, 0, 0),
    (314, 'IsActorAVictim', 0, 0, 0, 0),
    (313, 'IsActorEvil', 0, 0, 0, 0),
    (306, 'IsActorUsingATorch', 0, 0, 0, 0),
    (280, 'IsCellOwner', 2, 2, 0, 0),
    (267, 'IsCloudy', 0, 0, 0, 0),
    (150, 'IsContinuingPackagePCNear', 0, 0, 0, 0),
    (163, 'IsCurrentFurnitureObj', 2, 0, 0, 0),
    (162, 'IsCurrentFurnitureRef', 2, 0, 0, 0),
    (354, 'IsEssential', 0, 0, 0, 0),
    (106, 'IsFacingUp', 0, 0, 0, 0),
    (125, 'IsGuard', 0, 0, 0, 0),
    (282, 'IsHorseStolen', 0, 0, 0, 0),
    (112, 'IsIdlePlaying', 0, 0, 0, 0),
    (289, 'IsInCombat', 0, 0, 0, 0),
    (332, 'IsInDangerousWater', 0, 0, 0, 0),
    (300, 'IsInInterior', 0, 0, 0, 0),
    (146, 'IsInMyOwnedCell', 0, 0, 0, 0),
    (285, 'IsLeftUp', 0, 0, 0, 0),
    (278, 'IsOwner', 2, 0, 0, 0),
    (176, 'IsPCAMurderer', 0, 0, 0, 0),
    (175, 'IsPCSleeping', 0, 0, 0, 0),
    (358, 'IsPlayerMovingIntoNewSpace', 0, 0, 0, 0),
    (339, 'IsPlayersLastRiddenHorse', 0, 0, 0, 0),
    (266, 'IsPleasant', 0, 0, 0, 0),
    ( 62, 'IsRaining', 0, 0, 0, 0),
    (327, 'IsRidingHorse', 0, 0, 0, 0),
    (287, 'IsRunning', 0, 0, 0, 0),
    (103, 'IsShieldOut', 0, 0, 0, 0),
    (286, 'IsSneaking', 0, 0, 0, 0),
    ( 75, 'IsSnowing', 0, 0, 0, 0),
    (223, 'IsSpellTarget', 2, 0, 0, 0),
    (185, 'IsSwimming', 0, 0, 0, 0),
    (141, 'IsTalking', 0, 0, 0, 0),
    (265, 'IsTimePassing', 0, 0, 0, 0),
    (102, 'IsTorchOut', 0, 0, 0, 0),
    (145, 'IsTrespassing', 0, 0, 0, 0),
    (111, 'IsWaiting', 0, 0, 0, 0),
    (101, 'IsWeaponOut', 0, 0, 0, 0),
    (309, 'IsXBox', 0, 0, 0, 0),
    ( 36, 'MenuMode', 1, 0, 0, 0),
    ( 42, 'SameFaction', 2, 0, 0, 0),
    (133, 'SameFactionAsPC', 0, 0, 0, 0),
    ( 43, 'SameRace', 2, 0, 0, 0),
    (134, 'SameRaceAsPC', 0, 0, 0, 0),
    ( 44, 'SameSex', 2, 0, 0, 0),
    (135, 'SameSexAsPC', 0, 0, 0, 0),
    (323, 'WhichServiceMenu', 0, 0, 0, 0),
    (449, 'HasPerk', 2, 1, 1, 2),
    (546, 'GetQuestCompleted', 2, 0, 0, 0),
    (427, 'GetIsVoiceType', 2, 0, 0, 0),
    (523, 'IsPS3', 0, 0, 0, 0),
    (524, 'IsWin32', 0, 0, 0, 0),
    (372, 'IsInList', 2, 0, 0, 0),
    (382, 'GetHasNote', 2, 1, 1, 2),
    (492, 'GetMapMakerVisible', 1, 1, 1, 2),
    (446, 'GetInZone', 2, 1, 1, 2),
    ( 25, 'IsMoving', 0, 0, 0, 0),
    ( 26, 'IsTurning', 0, 0, 0, 0),
    (451, 'IsLastIdlePlayed', 2, 0, 0, 0),
    (399, 'IsWeaponInList', 2, 0, 0, 0),
    (408, 'GetVATSValue', 1, 2, 0, 0),
    (435, 'GetDialogueEmotion', 0, 0, 0, 0),
    (235, 'GetVatsTargetHeight', 0, 0, 0, 0),
    (391, 'GetHitLocation', 0, 0, 0, 0),
    (392, 'IsPC1stPerson', 0, 0, 0, 0),
    (226, 'GetSandman', 0, 0, 0, 0),
    (428, 'GetPlantedExplosive', 0, 0, 0, 0),
    (304, 'IsWaterObject', 0, 0, 0, 0),
    (123, 'IsGreetingPlayer', 0, 0, 0, 0),
    (438, 'GetIsCreatureType', 1, 0, 0, 0),
    (503, 'GetRadiationLevel', 0, 0, 0, 0),
    (431, 'GetHealthPercentage', 0, 0, 0, 0),
    (411, 'GetFactionCombatReaction', 2, 2, 0, 0),
    (515, 'IsCombatTarget', 2, 0, 0, 0),
    (495, 'GetPermanentActorValue', 1, 0, 0, 0),
    (474, 'GetIsAlignment', 1, 0, 0, 0),
    (454, 'GetPlayerTeammate', 0, 0, 0, 0),
    (522, 'GetIsLockBroken', 0, 0, 0, 0),
    (433, 'GetIsObjectType', 1, 0, 0, 0),
    (500, 'GetWeaponHealthPerc', 0, 0, 0, 0),
    (368, 'IsPlayerActionActive', 1, 0, 0, 0),
    (416, 'GetGroupMemberCount', 0, 0, 0, 0),
    (417, 'GetGroupTargetCount', 0, 0, 0, 0),
    (510, 'GetLastHitCritical', 0, 0, 0, 0),
    (450, 'GetFactionRelation', 1, 0, 0, 0),
    (455, 'GetPlayerTeammateCount', 0, 0, 0, 0),
    (219, 'GetAnimAction', 0, 0, 0, 0),
    (430, 'IsActorTalkingThroughActivator', 0, 0, 0, 0),
    (480, 'GetIsUsedItemEquipType', 1, 0, 0, 0),
    (398, 'IsLimbGone', 1, 0, 0, 0),
    (550, 'IsGoreDisabled', 0, 0, 0, 0),
    (420, 'GetObjectiveCompleted', 2, 1, 0, 0),
    (421, 'GetObjectiveDisplayed', 2, 1, 0, 0),
    (397, 'GetCauseofDeath', 0, 0, 0, 0),
    (415, 'Exists', 2, 0, 0, 0),
    (117, 'GetMajorCrimeCount', 0, 0, 0, 0),
    (471, 'GetDestructionStage', 0, 0, 0, 0),
    (460, 'GetActorFactionPlayerEnemy', 0, 0, 0, 0),

    # extended by FOSE
    (1024, 'GetFOSEVersion', 0, 0, 0, 0),
    (1025, 'GetFOSERevision', 0, 0, 0, 0),
    (1213, 'GetFOSEBeta', 0, 0, 0, 0),
    (1082, 'IsKeyPressed', 1, 0, 0, 0),
    (1166, 'IsControlPressed', 1, 0, 0, 0),
    (1028, 'GetWeight', 2, 0, 0, 0),
    (1165, 'GetWeaponHasScope', 0, 0, 0, 0),
    )