# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import Scraper


class Removed(Scraper):
    REASONS = {
        'jsh': 'Site is very JavaScript-heavy, writing a module would be' +
               ' very complicated.',
        'del': 'Comic was removed from the web.',
        'block': 'The comic site is blocking us.',
        'unk': 'Comic was removed for an unknown reason.',
        'brk': 'Comic navigation is broken.',
        'mov': 'Comic moved to a new hoster and no new module was written.',
        'mis': 'Pages are missing from the comic.',
        'acc': 'Account is needed to access site.',
    }

    def __init__(self, name, reason='del'):
        super(Removed, self).__init__(name)
        self.reason = reason

    def getDisabledReasons(self):
        return {'rem-' + self.reason: self.REASONS[self.reason]}

    @classmethod
    def getmodules(cls):
        return (
            # Removed in 2.16
            cls('AbleAndBaker'),
            cls('AlsoBagels'),
            cls('Antics'),
            cls('Arcamax/BleekerTheRechargeableDog'),
            cls('Arcamax/DeFlocked'),
            cls('Arcamax/TinasGroove'),
            cls('ASkeweredParadise'),
            cls('ASofterWorld', 'block'),
            cls('BackwaterPlanet'),
            cls('BigFatWhale'),
            cls('BizarreUprising'),
            cls('Blip'),
            cls('BoxerHockey'),
            cls('BoyOnAStickAndSlither', 'jsh'),
            cls('BrentalFloss'),
            cls('BrentalFloss/FlossedInTime'),
            cls('BrentalFloss/GuestComics'),
            cls('BrightlyWound'),
            cls('Caggage'),
            cls('Carciphona', 'jsh'),
            cls('Champ2010'),
            cls('CheckerboardNightmare'),
            # Patreon & Pixiv (https://www.patreon.com/Collar6)
            cls('Collar6', 'mov'),
            cls('ComicFury/30years'),
            cls('ComicFury/AAB'),
            cls('ComicFury/AdventuresofMaggie'),
            cls('ComicFury/Aether'),
            cls('ComicFury/Afairtrade'),
            cls('ComicFury/Afrodays'),
            cls('ComicFury/Albinobros'),
            cls('ComicFury/Alexanderandlucas'),
            cls('ComicFury/Alittlebitofeverything'),
            cls('ComicFury/Americanextremists'),
            cls('ComicFury/AmericanNerd'),
            cls('ComicFury/Amtheatre'),
            cls('ComicFury/Angstcomic'),
            cls('ComicFury/Applepine'),
            cls('ComicFury/Area42', 'mis'),
            cls('ComicFury/Atm'),
            cls('ComicFury/Atomicmonkey'),
            cls('ComicFury/Baseballcapsandtiaras'),
            cls('ComicFury/BATB'),
            cls('ComicFury/BetweenRounds'),
            cls('ComicFury/BigBookOfLameJokes'),
            cls('ComicFury/BiMorphon'),
            cls('ComicFury/Blessings'),
            cls('ComicFury/BrokenReality'),
            cls('ComicFury/BTTF'),
            cls('ComicFury/Cannonadeofhogwash'),
            cls('ComicFury/CatHero'),
            cls('ComicFury/Chocolava'),
            cls('ComicFury/ChristianHumberReloaded'),
            cls('ComicFury/Cockeyed'),
            cls('ComicFury/CoftheA'),
            cls('ComicFury/CompanyMan'),
            cls('ComicFury/Complicatedd'),
            cls('ComicFury/Conplicated'),
            cls('ComicFury/Crowbar'),
            cls('ComicFury/Crowbars'),
            cls('ComicFury/Curvyboneyosis'),
            cls('ComicFury/Dandk'),
            cls('ComicFury/Davidandtherobot'),
            cls('ComicFury/DenizensAttentionComic'),
            cls('ComicFury/Disturbingcomics'),
            cls('ComicFury/Docapoc'),
            cls('ComicFury/DucksMisery'),
            cls('ComicFury/Elfcomic'),
            cls('ComicFury/EMT'),
            cls('ComicFury/EternityC'),
            cls('ComicFury/Fathead'),
            cls('ComicFury/Fexpression'),
            cls('ComicFury/FireBorn2'),
            cls('ComicFury/Foxtales'),
            cls('ComicFury/Fpk'),
            cls('ComicFury/Ghostassassin'),
            cls('ComicFury/Gillimurphy'),
            cls('ComicFury/Glomshire'),
            cls('ComicFury/GodGames', 'mov'),
            cls('ComicFury/Goldrushdynllewcomics'),
            cls('ComicFury/Grandline3point5'),
            cls('ComicFury/Halloween2012'),
            cls('ComicFury/Halloween2013'),
            cls('ComicFury/HIRI'),
            cls('ComicFury/Hitmen'),
            cls('ComicFury/Honeyvenom'),
            cls('ComicFury/Insanitycorp'),
            cls('ComicFury/Inviziblecomixgroup'),
            cls('ComicFury/Isb'),
            cls('ComicFury/Its'),
            cls('ComicFury/Jenfferscartoonphotomanipulaion'),
            cls('ComicFury/Jenffersshow'),
            cls('ComicFury/Jeremy'),
            cls('ComicFury/Joysworldcomic'),
            cls('ComicFury/Judgedred'),
            cls('ComicFury/Jump2'),
            cls('ComicFury/Kachingcomic'),
            cls('ComicFury/Kazaandgwenna'),
            cls('ComicFury/Kevinzombie'),
            cls('ComicFury/Kindergardencrisis'),
            cls('ComicFury/Kirahitogame'),
            cls('ComicFury/Ladyspectra'),
            cls('ComicFury/Lastcallcomic'),
            cls('ComicFury/Lazy'),
            cls('ComicFury/Lena'),
            cls('ComicFury/Letitride'),
            cls('ComicFury/Lola2'),
            cls('ComicFury/LORDDARKE'),
            cls('ComicFury/Lp'),
            cls('ComicFury/LucidsDream'),
            cls('ComicFury/Lvl30psy'),
            cls('ComicFury/Maddog'),
            cls('ComicFury/Magisa'),
            cls('ComicFury/Midnightpeanutbutter'),
            cls('ComicFury/Minarga'),
            cls('ComicFury/MoizmadComix'),
            cls('ComicFury/Moths'),
            cls('ComicFury/MuttInTheMiddle'),
            cls('ComicFury/MyHorribleSite'),
            cls('ComicFury/Neighborscomic'),
            cls('ComicFury/Nojetpack'),
            cls('ComicFury/NoSongs'),
            cls('ComicFury/Nostalgiaofeden'),
            cls('ComicFury/Ocarinaoftim'),
            cls('ComicFury/OffHours'),
            cls('ComicFury/OldSchoolRasputinCatamite'),
            cls('ComicFury/Pandemonium'),
            cls('ComicFury/Paperstreamer'),
            cls('ComicFury/Peepsnperks'),
            cls('ComicFury/PersonaFTW'),
            cls('ComicFury/Pilgrimsprogress'),
            cls('ComicFury/PiratesLife'),
            cls('ComicFury/PobrePucho'),
            cls('ComicFury/Poussiere'),
            cls('ComicFury/Pt'),
            cls('ComicFury/Punch'),
            cls('ComicFury/Rangerrandom'),
            cls('ComicFury/Raspcat'),
            cls('ComicFury/RealLifeTrips'),
            cls('ComicFury/ReiketsuouNoKimi'),
            cls('ComicFury/RIDDICKQLOSSTALES'),
            cls('ComicFury/Romanjack'),
            cls('ComicFury/RPS'),
            cls('ComicFury/RPT'),
            cls('ComicFury/Rvr'),
            cls('ComicFury/Sarakleeyo'),
            cls('ComicFury/Sawbladersblacknuzlocke'),
            cls('ComicFury/Schizmatic'),
            cls('ComicFury/Seconds'),
            cls('ComicFury/Serengetti'),
            cls('ComicFury/SHADOWQUEEN'),
            cls('ComicFury/Shonenpunkremix'),
            cls('ComicFury/Sinjetpack'),
            cls('ComicFury/Spf1337'),
            cls('ComicFury/Sscomic'),
            cls('ComicFury/SteamSword'),
            cls('ComicFury/Teenagedragon'),
            cls('ComicFury/Theashes'),
            cls('ComicFury/TheButterflyEffect'),
            cls('ComicFury/Thecrease'),
            cls('ComicFury/TheGuardiansOfGrey'),
            cls('ComicFury/Tiziana'),
            cls('ComicFury/TwentyQuidAmusements'),
            cls('ComicFury/Underscore'),
            cls('ComicFury/ValtersRebellion'),
            cls('ComicFury/Wowwithatwistdamaclesandkejallcomic'),
            cls('ComicFury/YouAreNowEnteringAshburg'),
            cls('ComicGenesis/CryHavoc'),
            cls('ComicGenesis/IBlameDanny'),
            cls('ComicGenesis/SueosdelSur'),
            cls('Commissioned'),
            cls('CoolCatStudio'),
            cls('CowboyJedi', 'brk'),
            cls('Creators/BCinSpanish'),
            cls('Creators/GirlsandSportsinSpanish'),
            cls('Creators/Recess'),
            cls('Creators/RugratsinSpanish'),
            cls('CtrlAltDel', 'block'),
            cls('CtrlAltDel/Sillies', 'block'),
            cls('DailyDose'),
            cls('DamnLol'),
            cls('DeathToTheExtremist'),
            cls('DoctorCat', 'brk'),
            cls('DungeonsAndDenizens'),
            cls('EerieCuties'),
            cls('Ellerbisms'),
            cls('Eriadan'),
            cls('EverydayBlues'),
            cls('FeyWinds'),
            cls('FilibusterCartoons'),
            cls('FowlLanguage', 'block'),
            cls('GlassHalfEmpty'),
            cls('GoComics/ABootsAndPupComic'),
            cls('GoComics/AdventuresofDaisy'),
            cls('GoComics/AdventuresofMartyandTurkey'),
            cls('GoComics/AdventuresofMikeAndSimon'),
            cls('GoComics/AgentGates'),
            cls('GoComics/AlisonWard'),
            cls('GoComics/AmaZnEvents'),
            cls('GoComics/AnythingGoes'),
            cls('GoComics/BCEnEspaol'),
            cls('GoComics/BenAndSeymour'),
            cls('GoComics/BeneaththeFerns'),
            cls('GoComics/BenSargent'),
            cls('GoComics/BERSERKALERT'),
            cls('GoComics/BestInShow'),
            cls('GoComics/BiffAndRiley'),
            cls('GoComics/BillyAndCo'),
            cls('GoComics/BlackboardDaze'),
            cls('GoComics/BobtheGroanUP'),
            cls('GoComics/Boogerbrain'),
            cls('GoComics/BotBrothers'),
            cls('GoComics/BrilliantMines'),
            cls('GoComics/BuffaloChips'),
            cls('GoComics/BuzzaWuzza'),
            cls('GoComics/CafConLeche'),
            cls('GoComics/CalAndOzz'),
            cls('GoComics/CandyPills'),
            cls('GoComics/Cartertoons'),
            cls('GoComics/ChanLowe'),
            cls('GoComics/ChasingUnicorns'),
            cls('GoComics/ChubbyGirlComics'),
            cls('GoComics/Classifudds'),
            cls('GoComics/CleoandCompany'),
            cls('GoComics/CockroachComix'),
            cls('GoComics/CoffeeShopTidbits'),
            cls('GoComics/Cortoons'),
            cls('GoComics/CowSheepandaGnomeNamedHelga'),
            cls('GoComics/DabneyandDad'),
            cls('GoComics/DarrinBell'),
            cls('GoComics/DevinCraneComicStripGhostwriter'),
            cls('GoComics/DialHforHBomb'),
            cls('GoComics/DitzAbledPrincess'),
            cls('GoComics/DoodleDaysComics'),
            cls('GoComics/Dromo'),
            cls('GoComics/EBEJeebie'),
            cls('GoComics/EDITORIALPASTANDPRESENT'),
            cls('GoComics/ElephantintheRoom'),
            cls('GoComics/EleriMaiHarrisCartoons'),
            cls('GoComics/ElfandMotorbelly'),
            cls('GoComics/ElMundoDeBeakman'),
            cls('GoComics/EngagAndNevets'),
            cls('GoComics/EspressoCity'),
            cls('GoComics/EttoreandBaldo'),
            cls('GoComics/FantasticMegaLeague'),
            cls('GoComics/FarcesofNature'),
            cls('GoComics/Featherweight'),
            cls('GoComics/FrankBlunt'),
            cls('GoComics/FrizziToons'),
            cls('GoComics/FundayMorning'),
            cls('GoComics/GatorsAndSuch'),
            cls('GoComics/GenerationMute'),
            cls('GoComics/GentleCreatures'),
            cls('GoComics/GetAGrip'),
            cls('GoComics/GlennMcCoy'),
            cls('GoComics/GoComicsontheRoad'),
            cls('GoComics/HamShears'),
            cls('GoComics/HanginOut'),
            cls('GoComics/HankandDalesOurWorld'),
            cls('GoComics/HanktheSock'),
            cls('GoComics/HarambeeHills'),
            cls('GoComics/Hbenson7'),
            cls('GoComics/HeadComics'),
            cls('GoComics/HIP'),
            cls('GoComics/HolidayDoodles'),
            cls('GoComics/HolySchnark'),
            cls('GoComics/HoodootheUnwiseOwl'),
            cls('GoComics/Humoresque'),
            cls('GoComics/ImaDillo'),
            cls('GoComics/ImTellingMom'),
            cls('GoComics/InheritTheMirth'),
            cls('GoComics/JackRadioComics'),
            cls('GoComics/JayAndBoneheadTheMunkysMrCowhide'),
            cls('GoComics/JustPosted'),
            cls('GoComics/KatetheGreat'),
            cls('GoComics/KirbysTreehouse'),
            cls('GoComics/KozmooftheCosmos'),
            cls('GoComics/LardWantsWorldPeace'),
            cls('GoComics/LarryvilleBlue'),
            cls('GoComics/Leadbellies'),
            cls('GoComics/LegendofBill'),
            cls('GoComics/LeGooseyLu'),
            cls('GoComics/LeighLunaComics'),
            cls('GoComics/LIGHTERSIDE'),
            cls('GoComics/LostInTranslation'),
            cls('GoComics/Lucan'),
            cls('GoComics/LucasLuminous'),
            cls('GoComics/Mac'),
            cls('GoComics/Markonpaper'),
            cls('GoComics/MaryBWary'),
            cls('GoComics/MassiveFalls'),
            cls('GoComics/McArroni'),
            cls('GoComics/Mick'),
            cls('GoComics/MidLifewAlan'),
            cls('GoComics/Millennialhood'),
            cls('GoComics/MinimumSecurity'),
            cls('GoComics/MixedMedications'),
            cls('GoComics/Molebashed'),
            cls('GoComics/MollyandtheBear'),
            cls('GoComics/Mortimer'),
            cls('GoComics/MrGigiAndTheSquid'),
            cls('GoComics/MrMorris'),
            cls('GoComics/Mulligan'),
            cls('GoComics/MyGuardianGrandpa'),
            cls('GoComics/NavyBean'),
            cls('GoComics/NeatStep'),
            cls('GoComics/NedAndLarry'),
            cls('GoComics/NeighborhoodZone'),
            cls('GoComics/NobodysHome'),
            cls('GoComics/NoPlaceLikeHolmes'),
            cls('GoComics/Norman'),
            cls('GoComics/Oat'),
            cls('GoComics/ObamaandtheFatman'),
            cls('GoComics/OntheQuad'),
            cls('GoComics/OrangesareFunny'),
            cls('GoComics/Outnumbered'),
            cls('GoComics/ParisDoodles'),
            cls('GoComics/Peanizles'),
            cls('GoComics/PetFood'),
            cls('GoComics/Pi'),
            cls('GoComics/PigtimesCartoon'),
            cls('GoComics/PipethePelican'),
            cls('GoComics/PlanB'),
            cls('GoComics/PlasticBabyHeadsfromOuterSpace'),
            cls('GoComics/PlentyofPenguins'),
            cls('GoComics/Poptropica'),
            cls('GoComics/Putz'),
            cls('GoComics/QuestionsForKids'),
            cls('GoComics/RandomActsofNancy'),
            cls('GoComics/RedMeat'),
            cls('GoComics/RicigsToonTrivia'),
            cls('GoComics/RogueSymmetry'),
            cls('GoComics/Sabine'),
            cls('GoComics/SantavsDracula'),
            cls('GoComics/SCAIRYTALESTheNotSoScaryFairyTales'),
            cls('GoComics/Scurvyville'),
            cls('GoComics/SecondPrize'),
            cls('GoComics/Skooled'),
            cls('GoComics/SNAFU'),
            cls('GoComics/SouptoNutz'),
            cls('GoComics/SpaceNutz'),
            cls('GoComics/SPACESLUGS'),
            cls('GoComics/SpaceTimeFunnies'),
            cls('GoComics/Starslip'),
            cls('GoComics/STEPDAD'),
            cls('GoComics/Stookie'),
            cls('GoComics/SuburbanWilderness'),
            cls('GoComics/SuckerHeadSmack'),
            cls('GoComics/TeacherInk'),
            cls('GoComics/ThatMonkeyTune'),
            cls('GoComics/TheAcerbicCaf'),
            cls('GoComics/TheAdventuresofTeetyBallerina'),
            cls('GoComics/TheEdperiment'),
            cls('GoComics/TheFruitBowl'),
            cls('GoComics/TheGoldenKid'),
            cls('GoComics/TheInsolentLemon'),
            cls('GoComics/TheLightedLab'),
            cls('GoComics/TheLilMiesters'),
            cls('GoComics/TheOdderLimits'),
            cls('GoComics/THESILVERLINING'),
            cls('GoComics/TheSingleDadDiaries'),
            cls('GoComics/TheVernalPool'),
            cls('GoComics/TheWorstThingIveEverDone'),
            cls('GoComics/ThrompTM'),
            cls('GoComics/ToBeNamed'),
            cls('GoComics/TodaysDogg'),
            cls('GoComics/TonyAuth'),
            cls('GoComics/Toocrazy'),
            cls('GoComics/TOWHOMITMAYCONCERN'),
            cls('GoComics/Twaggies'),
            cls('GoComics/TwoBits'),
            cls('GoComics/Vernscartoons'),
            cls('GoComics/WayOutInLeftField'),
            cls('GoComics/WendlesLife'),
            cls('GoComics/Whatcatscanandcantdo'),
            cls('GoComics/WickedCrispy'),
            cls('GoComics/WindingRoads'),
            cls('GoComics/WitoftheWorld'),
            cls('GoComics/YouCanWithBeakmanAndJax'),
            cls('GoComics/YouGuysAreMyFriendsTheComic'),
            cls('GoComics/ZacharyNixonJohnson'),
            cls('GunnerkrigCourt'),
            cls('HorribleVille'),
            cls('JerkCity'),
            cls('KatzenfutterGeleespritzer'),
            cls('KeenSpot/Adventurers', 'mov'),
            cls('KeenSpot/Landis'),
            cls('Key'),
            cls('KillerKomics'),
            cls('Kukuburi'),
            cls('Lint'),
            cls('LinuxComFridayFunnies'),
            cls('NekkoAndJoruba'),
            cls('NekoTheKitty'),
            cls('NewAdventuresOfBobbin'),
            cls('Nnewts'),
            cls('OddFish'),
            cls('OneQuestion'),
            cls('OrnerBoy'),
            cls('PensAndTales/Evilish'),
            cls('PensAndTales/FireflyCross'),
            cls('PetiteSymphony/Kickinrad'),
            cls('PetiteSymphony/Orangegrind'),
            cls('PetiteSymphony/Seed'),
            cls('Pimpette'),
            cls('PunksAndNerds', 'mis'),
            cls('PunksAndNerdsOld'),
            # Moved to tapas.io, which blocks us
            cls('RadioactivePanda', 'block'),
            cls('RedsPlanet'),
            cls('RedString'),
            cls('SmackJeeves/Aarrevaara'),
            cls('SmackJeeves/AchievementStuck'),
            cls('SmackJeeves/AGirlAndHerShadow'),
            cls('SmackJeeves/Allthatglitters'),
            cls('SmackJeeves/AloversRule'),
            cls('SmackJeeves/Anathemacomics'),
            cls('SmackJeeves/AngelBeast'),
            cls('SmackJeeves/ArchportCityChronicles'),
            # moved to www.mgcomics.com, which has a robots.txt for everything
            cls('SmackJeeves/Aware', 'block'),
            cls('SmackJeeves/AwesomeSauce'),
            cls('SmackJeeves/Babywhatsyoursign'),
            cls('SmackJeeves/BetweenLightandDark'),
            cls('SmackJeeves/BetweenWorlds'),
            cls('SmackJeeves/BeyondTemptation'),
            cls('SmackJeeves/BLDShortComics'),
            cls('SmackJeeves/Bloodyfairytale'),
            cls('SmackJeeves/BLOT'),
            cls('SmackJeeves/BlueWell'),
            cls('SmackJeeves/BreakfastonaCliff'),
            cls('SmackJeeves/CafeAmargo'),
            cls('SmackJeeves/Captor'),
            cls('SmackJeeves/ChaosTheory2005'),
            cls('SmackJeeves/CleanCure'),
            cls('SmackJeeves/DaddysGirl'),
            cls('SmackJeeves/DeadtoDay'),
            cls('SmackJeeves/Debtsettlement'),
            cls('SmackJeeves/DebtSettlement2OperationExtinction'),
            cls('SmackJeeves/DefyingGravityTheFourGreatGuardians'),
            cls('SmackJeeves/Destinationunknown'),
            cls('SmackJeeves/DevilTrainee'),
            cls('SmackJeeves/DevilTraineeSpanish'),
            cls('SmackJeeves/Diexemor'),
            cls('SmackJeeves/DigisRandomSpriteshack'),
            cls('SmackJeeves/DontDie'),
            cls('SmackJeeves/ElfenLiedDifferences'),
            cls('SmackJeeves/Entuthrie'),
            cls('SmackJeeves/EozinKadonnutKuningas'),
            cls('SmackJeeves/EpicChaos'),
            cls('SmackJeeves/EternalKnights'),
            cls('SmackJeeves/EvD'),
            cls('SmackJeeves/FatetheAnthologyofKaienandhisfuckingmagicfriends'),
            cls('SmackJeeves/FeathersPI'),
            cls('SmackJeeves/FemmeSchism'),
            cls('SmackJeeves/FireWire'),
            cls('SmackJeeves/FrenzyRedux'),
            cls('SmackJeeves/FrogKing'),
            cls('SmackJeeves/FuckMyLife'),
            cls('SmackJeeves/FurtherDowntheRabbitHole'),
            cls('SmackJeeves/GATEKEEPER'),
            cls('SmackJeeves/GearTheTakedown'),
            cls('SmackJeeves/GoldenSunGenerationsAftermathVolume1'),
            cls('SmackJeeves/GoldenSunGenerationsColossoVolume6'),
            cls('SmackJeeves/GraveImpressions'),
            cls('SmackJeeves/GreenKirbyandabunchofotherpeopledoinstuff'),
            cls('SmackJeeves/GuardianGhost'),
            cls('SmackJeeves/Harfang'),
            cls('SmackJeeves/HIPS'),
            cls('SmackJeeves/HitandMiss'),
            cls('SmackJeeves/HotChocolate'),
            cls('SmackJeeves/Hybristorific'),
            cls('SmackJeeves/Ianua'),
            cls('SmackJeeves/ImminentMoose'),
            cls('SmackJeeves/InthePride'),
            cls('SmackJeeves/Intoxicated'),
            cls('SmackJeeves/Jantarpol'),
            cls('SmackJeeves/Knife'),
            cls('SmackJeeves/Kranburn'),
            cls('SmackJeeves/KuroNeko'),
            cls('SmackJeeves/LastLivingSouls'),
            cls('SmackJeeves/LegendsofMobiusBookOne'),
            cls('SmackJeeves/LetsBreakitforReals'),
            cls('SmackJeeves/LiliBleu'),
            cls('SmackJeeves/LoveTwister'),
            cls('SmackJeeves/MagicalGirlAlice'),
            cls('SmackJeeves/MasqueradeWTTM'),
            cls('SmackJeeves/MegaManBattleNetwork7'),
            cls('SmackJeeves/MegaManiacs'),
            cls('SmackJeeves/MerirosvotSeikkailumerella'),
            cls('SmackJeeves/MewsDynasty'),
            cls('SmackJeeves/MixupofallMixups'),
            cls('SmackJeeves/MomthegamestorerippedusoffAGAIN'),
            cls('SmackJeeves/MoonlitDawnAMythicalTale'),
            cls('SmackJeeves/MUTE', 'mov'),
            cls('SmackJeeves/MyBoyfriendisaMobBoss'),
            cls('SmackJeeves/MyTrollLife'),
            cls('SmackJeeves/MyTwoCentsPlusTax'),
            cls('SmackJeeves/NeoCrystalAdventures'),
            cls('SmackJeeves/NihilWandasJourney'),
            cls('SmackJeeves/OddContact'),
            cls('SmackJeeves/Ohman', 'brk'),
            cls('SmackJeeves/OneFrameGags'),
            cls('SmackJeeves/Pahantekija'),
            cls('SmackJeeves/Paradox'),
            cls('SmackJeeves/Paripety'),
            cls('SmackJeeves/Perinto'),
            cls('SmackJeeves/PerplexingMagnoliaDisruption', 'mov'),
            cls('SmackJeeves/PlatonicBoyfriends'),
            cls('SmackJeeves/Plotlessnesses'),
            cls('SmackJeeves/PokemonGleamingCrystal', 'mis'),
            cls('SmackJeeves/PokemonMysteryDungeonTeamCrystal'),
            cls('SmackJeeves/PRAGUERACE'),
            cls('SmackJeeves/PumpkinFlower'),
            cls('SmackJeeves/Razor'),
            cls('SmackJeeves/RedVelvetRequiem'),
            cls('SmackJeeves/RuderiQuest'),
            cls('SmackJeeves/SAKANA'),
            cls('SmackJeeves/SenoireDelirium'),
            cls('SmackJeeves/SerendipityAnEquestrianTale'),
            cls('SmackJeeves/ShacklesInstallment02'),
            cls('SmackJeeves/SimonSues'),
            cls('SmackJeeves/SimplySarah'),
            cls('SmackJeeves/SomebodyShootMe'),
            cls('SmackJeeves/SonicUniverseAsk'),
            cls('SmackJeeves/SoulGuardian'),
            cls('SmackJeeves/SpaghettiAndMeatballs'),
            cls('SmackJeeves/SparkStory', 'mis'),
            cls('SmackJeeves/Spidersilk', 'mov'),
            cls('SmackJeeves/Symbios'),
            cls('SmackJeeves/TechnicolorLondon'),
            cls('SmackJeeves/TeKscloset'),
            cls('SmackJeeves/TheAttackoftheRecoloursSeason1'),
            cls('SmackJeeves/TheAvianStories'),
            cls('SmackJeeves/TheCurtandTonyShow'),
            cls('SmackJeeves/TheDarkAgeofMobius'),
            cls('SmackJeeves/TheHobbitbic'),
            cls('SmackJeeves/ThehumanBEing'),
            cls('SmackJeeves/TheKeyToReality'),
            cls('SmackJeeves/TheLostland'),
            cls('SmackJeeves/TheMewExperiment'),
            cls('SmackJeeves/TheMoistTouch'),
            cls('SmackJeeves/TheRandomObscureFairyTaleNoOnesEverReallyHeardOf'),
            cls('SmackJeeves/TheSomewhereOther'),
            cls('SmackJeeves/TheWastelands', 'mis'),
            cls('SmackJeeves/ThinkBeforeYouThink', 'mov'),
            cls('SmackJeeves/ThroughTheWonkyEye'),
            cls('SmackJeeves/TitleUnrelated'),
            cls('SmackJeeves/TotalPokemonIsland'),
            cls('SmackJeeves/TrillyAndSilly'),
            cls('SmackJeeves/TRIPP'),
            cls('SmackJeeves/VampireFetish'),
            cls('SmackJeeves/WolfWolf'),
            cls('SmackJeeves/WonderTheatre'),
            cls('SmackJeeves/YouAreTheReasonForTheEndOfTheWorld'),
            cls('SnowFlakes'),
            cls('StrawberryDeathCake'),
            cls('Stubble'),
            cls('SuburbanTribe'),
            cls('TheOuterQuarter'),
            cls('TheParkingLotIsFull'),
            cls('TheThinHLine', 'acc'),
            cls('ThunderAndLightning'),
            cls('TinyKittenTeeth'),
            cls('TwoTwoOneFour'),
            cls('VampireCheerleaders'),
            cls('WayfarersMoon'),
            cls('WebcomicEu/Talandor'),
            cls('WebcomicEu/TheBessEffect'),
            cls('WebcomicEu/TheBessEffectEnglish'),
            cls('WebcomicsNation/AgnesQuill'),
            cls('WebcomicsNation/MyMuse'),
            cls('WebcomicsNation/NekkoAndJoruba'),
            cls('WeCanSleepTomorrow'),
            cls('WhiteNinja'),
            cls('WLP/ShadowChasers'),
            cls('WotNow'),
        )


class Renamed(Scraper):
    MSG = 'Comic module was renamed to "%s", please rename the directory.'
    count = 0

    @classmethod
    def counter(cls):
        cls.count += 1
        return cls.count

    def __init__(self, name, newname):
        super(Renamed, self).__init__(name)
        self.newname = newname
        self.i = self.counter()

    def getDisabledReasons(self):
        return {'ren-%i' % self.i: self.MSG % self.newname}

    @classmethod
    def getmodules(cls):
        return (
            # Renamed in 2.16
            cls('1997', '1977'),
            cls('ApartmentForTwo', 'NamirDeiter/ApartmentForTwo'),
            cls('Catena', 'CatenaManor/CatenaCafe'),
            cls('ComicFury/Alya', 'ComicFury/AlyaTheLastChildOfLight'),
            cls('ComicFury/Boatcrash', 'ComicFury/BoatcrashChronicles'),
            cls('ComicFury/Crimsonpixel', 'ComicFury/CrimsonPixelComics'),
            cls('ComicFury/Doublejump', 'ComicFury/DoubleJumpGameComics'),
            cls('ComicFury/Elektroanthology', 'ComicFury/ElektrosComicAnthology'),
            cls('ComicFury/ICanSeeYourFeels', 'ComicFury/SeeYourFeels'),
            cls('ComicFury/MAGISAupdatesMonWedFri', 'ComicFury/MAGISAPARASAYOupdatesMonFri'),
            cls('ComicFury/OopsComicAdventure', 'OopsComicAdventure'),
            cls('ComicFury/ThomasAndZachary', 'ComicFury/ThomasAndZacharyArchives'),
            cls('ComicGenesis/TheLounge', 'KeenSpot/TheLounge'),
            cls('Creators/ArchieinSpanish', 'Creators/ArchieSpanish'),
            cls('Creators/HeathcliffinSpanish', 'Creators/HeathcliffSpanish'),
            cls('Creators/TheWizardofIdinSpanish', 'Creators/WizardOfIdSpanish'),
            cls('DarkWings', 'Eryl'),
            cls('EyeOfRamalach', 'KemonoCafe/TheEyeOfRamalach'),
            cls('FoulLanguage', 'GoComics/FowlLanguage'),
            cls('GoComics/060', 'ComicSherpa/060'),
            cls('GoComics/ABitSketch', 'ComicSherpa/ABitSketch'),
            cls('GoComics/Andnow', 'ComicSherpa/AndNow'),
            cls('GoComics/Anecdote', 'ComicSherpa/Anecdote'),
            cls('GoComics/AppleCreekComics', 'ComicSherpa/AppleCreekComics'),
            cls('GoComics/BarkingCrayon', 'ComicFury/BarkingCrayon'),
            cls('GoComics/BatchRejection', 'ComicSherpa/BatchRejection'),
            cls('GoComics/Bazoobee', 'ComicSherpa/Bazoobee'),
            cls('GoComics/Bluebonnets', 'ComicSherpa/Bluebonnets'),
            cls('GoComics/BlueSkiesToons', 'ComicSherpa/BlueSkiesToons'),
            cls('GoComics/BottAuto', 'ComicSherpa/BottAuto'),
            cls('GoComics/BUNS', 'ComicSherpa/BUNS'),
            cls('GoComics/CAFFEINATED', 'ComicSherpa/CAFFEINATED'),
            cls('GoComics/CharmysArmy', 'ComicSherpa/CharmysArmy'),
            cls('GoComics/CourageousManAdventures', 'ComicSherpa/CourageousManAdventures'),
            cls('GoComics/DontPicktheFlowers', 'ComicSherpa/DontPickTheFlowers'),
            cls('GoComics/Dragin', 'ComicSherpa/Dragin'),
            cls('GoComics/DumbQuestionBadAnswer', 'ComicSherpa/DumbQuestionBadAnswer'),
            cls('GoComics/DustSpecks', 'ComicSherpa/DustSpecks'),
            cls('GoComics/Econogirl', 'ComicSherpa/Econogirl'),
            cls('GoComics/Elmo', 'ComicSherpa/Elmo'),
            cls('GoComics/FarOut', 'ComicSherpa/FarOut'),
            cls('GoComics/FrankAndSteinway', 'ComicSherpa/FrankAndSteinway'),
            cls('GoComics/FriedCritter', 'ComicSherpa/FriedCritter'),
            cls('GoComics/GarciaCartoonCo', 'ComicSherpa/GarciaCartoonCo'),
            cls('GoComics/GIRTH', 'ComicSherpa/GIRTH'),
            cls('GoComics/GrannyAnny', 'ComicSherpa/GrannyAnny'),
            cls('GoComics/GreenPieces', 'ComicSherpa/GreenPieces'),
            cls('GoComics/GunstonStreet', 'ComicSherpa/GunstonStreet'),
            cls('GoComics/Headcheese', 'ComicSherpa/Headcheese'),
            cls('GoComics/ItsjustJim', 'ComicSherpa/ItsJustJim'),
            cls('GoComics/JillpokeBohemia', 'ComicFury/JillpokeBohemia'),
            cls('GoComics/KartoonsByKline', 'ComicSherpa/KartoonsByKline'),
            cls('GoComics/LumandAbner', 'ComicSherpa/LumAndAbner'),
            cls('GoComics/Millennialville', 'ComicSherpa/Millennialville'),
            cls('GoComics/Milton50', 'ComicSherpa/Milton50'),
            cls('GoComics/Mindframe', 'ComicSherpa/Mindframe'),
            cls('GoComics/MiscSoup', 'ComicSherpa/MiscSoup'),
            cls('GoComics/MisterAndMe', 'ComicSherpa/MisterAndMe'),
            cls('GoComics/MortsIsland', 'ComicSherpa/MortsIsland'),
            cls('GoComics/NoOrdinaryLife', 'ComicSherpa/NoOrdinaryLife'),
            cls('GoComics/ONIONAndPEA', 'ComicSherpa/ONIONAndPEA'),
            cls('GoComics/PaddedCell', 'ComicSherpa/PaddedCell'),
            cls('GoComics/Peeples', 'ComicSherpa/Peeples'),
            cls('GoComics/PirateMike', 'ComicSherpa/PirateMike'),
            cls('GoComics/PoliceLimit', 'ComicSherpa/PoliceLimit'),
            cls('GoComics/RonWarren', 'ComicSherpa/RonWarren'),
            cls('GoComics/SignGarden', 'ComicSherpa/SignGarden'),
            cls('GoComics/SleepytownBeagles', 'ComicSherpa/SleepytownBeagles'),
            cls('GoComics/SmallNerdyCreatures', 'ComicSherpa/SmallNerdyCreatures'),
            cls('GoComics/Smith', 'ComicSherpa/Smith'),
            cls('GoComics/SoccerEarth', 'ComicSherpa/SoccerEarth'),
            cls('GoComics/SookyRottweiler', 'ComicSherpa/SookyRottweiler'),
            cls('GoComics/SportsbyVoort', 'ComicSherpa/SportsByVoort'),
            cls('GoComics/StankoAndTibor', 'ComicSherpa/StankoAndTibor'),
            cls('GoComics/SubSub', 'ComicSherpa/SubSub'),
            cls('GoComics/SuburbanFairyTales', 'ComicSherpa/SuburbanFairyTales'),
            cls('GoComics/SuperSiblings', 'ComicSherpa/SuperSiblings'),
            cls('GoComics/TheBeauforts', 'ComicSherpa/TheBeauforts'),
            cls('GoComics/TheBoobiehatch', 'ComicSherpa/TheBoobiehatch'),
            cls('GoComics/TheCardinal', 'ComicSherpa/TheCardinal'),
            cls('GoComics/TheGreenMonkeys', 'ComicSherpa/TheGreenMonkeys'),
            cls('GoComics/TheOldManAndHisDog', 'ComicSherpa/TheOldManAndHisDog'),
            cls('GoComics/TheQuinnAndFinnShow', 'ComicSherpa/TheQuinnAndFinnShow'),
            cls('GoComics/Thingsesque', 'ComicSherpa/Thingsesque'),
            cls('GoComics/WayOutComics', 'ComicSherpa/WayOutComics'),
            cls('GoComics/WhiskeyFalls', 'ComicSherpa/WhiskeyFalls'),
            cls('GoComics/Wrobbertcartoons', 'ComicSherpa/WrobbertCartoons'),
            cls('GoComics/Zootopia', 'ComicSherpa/Zootopia'),
            cls('KeenSpot/AntiheroForHire', 'AntiheroForHire'),
            cls('KeenSpot/ElGoonishShive', 'ElGoonishShive'),
            cls('KeenSpot/ElGoonishShiveNP', 'ElGoonishShiveNP'),
            cls('KeenSpot/Newshounds', 'Newshounds'),
            cls('KeenSpot/SinFest', 'SinFest'),
            cls('KeenSpot/TheGodChild', 'GodChild'),
            cls('LasLindas', 'KemonoCafe/LasLindas'),
            cls('NicoleAndDerek', 'NamirDeiter/NicoleAndDerek'),
            cls('OnTheFasttrack', 'ComicsKingdom/OnTheFastrack'),
            cls('PetiteSymphony/Djandora', 'ComicsBreak/Djandora'),
            cls('PetiteSymphony/Generation17', 'ComicsBreak/Generation17'),
            cls('PetiteSymphony/Rascals', 'KemonoCafe/Rascals'),
            cls('QuentynQuinnSpaceRanger', 'RHJunior/QuentynQuinnSpaceRanger'),
            cls('ShermansLagoon', 'ComicsKingdom/ShermansLagoon'),
            cls('SmackJeeves/AddictiveScience', 'KemonoCafe/AddictiveScience'),
            cls('SmackJeeves/CityFolk', 'ComicFury/CityFolk'),
            cls('SmackJeeves/DoomsdayMyDear', 'DoomsdayMyDear'),
            cls('SmackJeeves/ForestHill', 'ForestHill'),
            cls('SmackJeeves/Katran', 'ComicFury/KATRAN'),
            cls('SmackJeeves/LatchkeyKingdom', 'ComicFury/LatchkeyKingdom'),
            cls('SmackJeeves/Magience', 'ComicFury/Magience'),
            cls('SmackJeeves/RiversideExtras', 'RiversideExtras'),
            cls('SmackJeeves/StarTrip', 'StarTrip'),
            cls('TalesOfTheQuestor', 'RHJunior/TalesOfTheQuestor'),
            cls('TheProbabilityBomb', 'RHJunior/TheProbabilityBomb'),
            cls('TracyAndTristan', 'ComicFury/TracyAndTristan'),
            cls('UnlikeMinerva', 'NamirDeiter/UnlikeMinerva'),
            cls('Wulffmorgenthaler', 'WuMo'),
            cls('YouSayItFirst', 'NamirDeiter/YouSayItFirst'),
            cls('ZebraGirl', 'ComicFury/ZebraGirl'),
        )
