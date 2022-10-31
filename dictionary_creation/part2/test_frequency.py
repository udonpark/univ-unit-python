"""Unit Testing for Task 1 and 2"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '30/05/2020'
__since__ = '22/05/2020'

import unittest
import sys
from hash_table import LinearProbeHashTable
from frequency import Frequency, Rarity


class TestFrequency(unittest.TestCase):
    def setUp(self) -> None:
        self.frequency = Frequency()

    def test_init(self) -> None:
        self.assertEqual(type(self.frequency.hash_table), LinearProbeHashTable)
        self.assertEqual(self.frequency.dictionary.find_word('test'), 1)

    def test_add_file(self) -> None:
        """
        Test 1 on add_file.
        I have created new instance of Frequency and set as t1, for convenience
        I have made new test1.txt as well
        """
        t1 = Frequency()
        t1.add_file("test1.txt")  
        self.assertEqual(t1.hash_table["a"], 2) # a is found twice in the test1.txt
        self.assertEqual(t1.hash_table["add"], 1)  # ADD must be counted as add, lowercase

    def test_rarity(self) -> None:
        """
        My second test using t2
        """
        t2 = Frequency()
        t2.add_file("test1.txt")
        self.assertEqual(t2.rarity("b"), Rarity.COMMON)  # It must have output common rarity
        self.assertEqual(t2.rarity("lkjhggj"), Rarity.MISSPELT)  # this word is not in dictionary, so should print MISSPELT


    def test_ranking(self) -> None:
        sys.setrecursionlimit(50000)
        self.frequency.add_file('215-0.txt')
        expected_output = [('the', 334), ('and', 220), ('he', 162), ('of', 123), ('was', 122), ('a', 115), ('to', 82), ('his', 80), ('in', 74), ('that', 52), ('at', 45), ('had', 43), ('with', 43), ('it', 42), ('him', 42), ('buck', 41), ('for', 37), ('not', 33), ('on', 31), ('but', 30), ('man', 30), ('were', 26), ('by', 26), ('from', 25), ('as', 24), ('them', 24), ('they', 24), ('into', 23), ('dogs', 19), ('an', 19), ('one', 18), ('this', 18), ('all', 17), ('men', 17), ('did', 16), ('when', 16), ('no', 15), ('so', 15), ('or', 15), ('there', 15), ('be', 14), ('club', 13), ('again', 12), ('out', 12), ('who', 12), ('knew', 12), ('himself', 11), ('hand', 11), ('which', 11), ('would', 10), ('came', 10), ('life', 10), ('more', 10), ('curly', 10), ('you', 10), ('back', 10), ('been', 10), ('down', 10), ('nor', 10), ('never', 10), ('went', 9), ('saw', 9), ('chapter', 9), ('time', 9), ('upon', 9), ('two', 9), ('other', 9), ('off', 9), ('dog', 9), ('her', 8), ('crate', 8), ('first', 8), ('where', 8), ('though', 8), ('way', 8), ('over', 8), ('through', 8), ('rope', 8), ('red', 7), ('i', 7), ('then', 7), ('sweater', 7), ('judge', 7), ('their', 7), ('while', 7), ('last', 7), ('tongue', 7), ('like', 7), ('under', 6), ('days', 6), ('four', 6), ('neck', 6), ('made', 6), ('wild', 6), ('feet', 6), ('up', 6), ('brought', 6), ('nights', 6), ('laughed', 5), ('some', 5), ('away', 5), ('could', 5), ('money', 5), ('go', 5), ('get', 5), ('too', 5), ('before', 5), ('shock', 5), ('sprang', 5), ('eyes', 5), ('took', 5), ('what', 5), ('half', 5), ('long', 5), ('lived', 5), ('another', 5), ('learned', 5), ('throat', 5), ('nothing', 5), ('air', 5), ('neither', 5), ('call', 5), ('little', 5), ('express', 5), ('manuel', 5), ('she', 5), ('law', 5), ('hundred', 5), ('lay', 5), ('car', 4), ('great', 4), ('leap', 4), ('around', 4), ('next', 4), ('forty', 4), ('between', 4), ('alone', 4), ('have', 4), ('ground', 4), ('carried', 4), ('do', 4), ('place', 4), ('looked', 4), ('right', 4), ('hatchet', 4), ('see', 4), ('teeth', 4), ('each', 4), ('dignity', 4), ('night', 4), ('these', 4), ('flung', 4), ('met', 4), ('its', 4), ('times', 4), ('wagon', 4), ('even', 4), ('morning', 4), ('narwhal', 4), ('face', 4), ('is', 4), ('fair', 4), ('know', 4), ('bloody', 4), ('said', 4), ('because', 4), ('about', 4), ('water', 4), ('day', 4), ('boys', 4), ('chest', 3), ('felt', 3), ('primitive', 3), ('well', 3), ('gutenberg', 3), ('wrath', 3), ('ate', 3), ('london', 3), ('things', 3), ('drank', 3), ('mouth', 3), ('once', 3), ('against', 3), ('only', 3), ('take', 3), ('driver', 3), ('often', 3), ('project', 3), ('every', 3), ('spitz', 3), ('seen', 3), ('house', 3), ('set', 3), ('play', 3), ('till', 3), ('hair', 3), ('strange', 3), ('growled', 3), ('threw', 3), ('head', 3), ('left', 3), ('here', 3), ('struck', 3), ('anger', 3), ('nose', 3), ('understand', 3), ('performance', 3), ('wanted', 3), ('big', 3), ('instant', 3), ('horses', 3), ('creatures', 3), ('very', 3), ('called', 3), ('ran', 3), ('sleep', 3), ('lesson', 3), ('fashion', 3), ('why', 3), ('trouble', 3), ('pride', 3), ('received', 3), ('fell', 3), ('after', 3), ('thing', 3), ('toots', 3), ('now', 3), ('almost', 3), ('blow', 3), ('many', 3), ('fang', 3), ('advances', 3), ('same', 3), ('also', 3), ('strong', 3), ('bars', 3), ('rushed', 3), ('reply', 3), ('during', 3), ('jack', 3), ('whip', 2), ('sled', 2), ('fellow', 2), ('among', 2), ('such', 2), ('good', 2), ('aspect', 2), ('grew', 2), ('most', 2), ('front', 2), ('can', 2), ('father', 2), ('cold', 2), ('rush', 2), ('cool', 2), ('pain', 2), ('silent', 2), ('pass', 2), ('years', 2), ('united', 2), ('taken', 2), ('jaw', 2), ('toil', 2), ('pent', 2), ('shed', 2), ('closed', 2), ('kind', 2), ('kept', 2), ('seattle', 2), ('spring', 2), ('collar', 2), ('besetting', 2), ('less', 2), ('intent', 2), ('if', 2), ('hurled', 2), ('utterly', 2), ('passage', 2), ('fear', 2), ('berry', 2), ('eh', 2), ('huskies', 2), ('rolled', 2), ('charge', 2), ('unwonted', 2), ('waxed', 2), ('warm', 2), ('dragged', 2), ('fire', 2), ('tank', 2), ('quiet', 2), ('bark', 2), ('body', 2), ('moment', 2), ('grooms', 2), ('watched', 2), ('government', 2), ('mercilessly', 2), ('hands', 2), ('let', 2), ('suffering', 2), ('yard', 2), ('included', 2), ('experience', 2), ('along', 2), ('together', 2), ('unfair', 2), ('senses', 2), ('added', 2), ('clip', 2), ('dozen', 2), ('least', 2), ('work', 2), ('english', 2), ('love', 2), ('any', 2), ('stranger', 2), ('struggle', 2), ('broken', 2), ('later', 2), ('faced', 2), ('valley', 2), ('tormentors', 2), ('home', 2), ('known', 2), ('newspapers', 2), ('decided', 2), ('steamer', 2), ('ill', 2), ('bristling', 2), ('weazened', 2), ('stood', 2), ('beaten', 2), ('stout', 2), ('strike', 2), ('aware', 2), ('heavy', 2), ('new', 2), ('strangers', 2), ('your', 2), ('located', 2), ('ends', 2), ('contents', 2), ('twice', 2), ('obedience', 2), ('surprise', 2), ('best', 2), ('endured', 2), ('true', 2), ('swarthy', 2), ('sound', 2), ('are', 2), ('terriers', 2), ('pounds', 2), ('wall', 2), ('strength', 2), ('quick', 2), ('yawned', 2), ('respect', 2), ('caught', 2), ('merely', 2), ('tightened', 2), ('wise', 2), ('licked', 2), ('propeller', 2), ('white', 2), ('friendly', 2), ('than', 2), ('fury', 2), ('spoke', 2), ('experienced', 2), ('manner', 2), ('much', 2), ('ii', 2), ('deck', 2), ('primordial', 2), ('give', 2), ('caused', 2), ('patches', 2), ('messengers', 2), ('train', 2), ('close', 2), ('began', 2), ('turned', 2), ('states', 2), ('dazed', 2), ('introduction', 2), ('snow', 2), ('launched', 2), ('read', 2), ('has', 2), ('talked', 2), ('wide', 2), ('roaring', 2), ('born', 2), ('choked', 2), ('baggage', 2), ('put', 2), ('open', 2), ('world', 2), ('glad', 2), ('being', 2), ('wheeler', 2), ('circle', 2), ('end', 2), ('agony', 2), ('fine', 2), ('hunting', 2), ('system', 2), ('country', 2), ('cried', 2), ('animal', 2), ('heart', 2), ('san', 2), ('snarling', 2), ('raging', 2), ('wolf', 2), ('jaws', 2), ('chunk', 2), ('muscles', 2), ('halfway', 2), ('meal', 2), ('ripped', 2), ('finally', 2), ('husky', 1), ('august', 1), ('puppyhood', 1), ('harness', 1), ('driveways', 1), ('three', 1), ('coat', 1), ('realm', 1), ('trace', 1), ('charlotte', 1), ('food', 1), ('rebel', 1), ('foot', 1), ('brewing', 1), ('we', 1), ('japanese', 1), ('form', 1), ('bully', 1), ('foul', 1), ('comprehend', 1), ('language', 1), ('docilely', 1), ('quivering', 1), ('metamorphosed', 1), ('memorable', 1), ('travel', 1), ('boomed', 1), ('watch', 1), ('carted', 1), ('arrangement', 1), ('furiously', 1), ('count', 1), ('july', 1), ('relief', 1), ('come', 1), ('cover', 1), ('furry', 1), ('become', 1), ('royal', 1), ('size', 1), ('copy', 1), ('aback', 1), ('sated', 1), ('adventures', 1), ('needs', 1), ('resided', 1), ('growls', 1), ('grass', 1), ('credit', 1), ('book', 1), ('vague', 1), ('reign', 1), ('retaliated', 1), ('boss', 1), ('excited', 1), ('universal', 1), ('obey', 1), ('sense', 1), ('wherever', 1), ('transportation', 1), ('saved', 1), ('joined', 1), ('cost', 1), ('given', 1), ('wood', 1), ('sharp', 1), ('receding', 1), ('drew', 1), ('pumping', 1), ('agonizing', 1), ('advantage', 1), ('surging', 1), ('fiend', 1), ('staggered', 1), ('fund', 1), ('mass', 1), ('title', 1), ('whoever', 1), ('grinned', 1), ('advanced', 1), ('eagerly', 1), ('unbridled', 1), ('crack', 1), ('instance', 1), ('narrow', 1), ('annoyed', 1), ('fifty', 1), ('arctic', 1), ('aroused', 1), ('cayuses', 1), ('fight', 1), ('passion', 1), ('wrap', 1), ('gentlemen', 1), ('tuition', 1), ('mangled', 1), ('ashamed', 1), ('v', 1), ('grumbled', 1), ('complete', 1), ('pitched', 1), ('driving', 1), ('rattled', 1), ('snort', 1), ('sensation', 1), ('mess', 1), ('outhouses', 1), ('crawling', 1), ('equally', 1), ('darkness', 1), ('legion', 1), ('glimpses', 1), ('veranda', 1), ('buried', 1), ('administering', 1), ('kidnapper', 1), ('bored', 1), ('fierce', 1), ('picked', 1), ('soliloquized', 1), ('surprised', 1), ('looking', 1), ('yellow', 1), ('sticks', 1), ('smiled', 1), ('aside', 1), ('just', 1), ('mine', 1), ('fanned', 1), ('iv', 1), ('approached', 1), ('fallen', 1), ('sinking', 1), ('sons', 1), ('brooms', 1), ('updated', 1), ('glitter', 1), ('peculiar', 1), ('commented', 1), ('asked', 1), ('recognized', 1), ('breath', 1), ('facts', 1), ('spacious', 1), ('tails', 1), ('undesirable', 1), ('hunger', 1), ('onlookers', 1), ('forest', 1), ('guarded', 1), ('yelped', 1), ('busy', 1), ('inside', 1), ('me', 1), ('carry', 1), ('beautiful', 1), ('diego', 1), ('becoming', 1), ('eloquently', 1), ('punish', 1), ('trees', 1), ('booming', 1), ('boxes', 1), ('axe', 1), ('doubled', 1), ('intimate', 1), ('forgot', 1), ('bid', 1), ('lack', 1), ('bit', 1), ('started', 1), ('paddocks', 1), ('deposited', 1), ('breathed', 1), ('instantaneous', 1), ('mops', 1), ('cement', 1), ('keep', 1), ('replied', 1), ('safety', 1), ('matter', 1), ('produced', 1), ('uproariously', 1), ('dam', 1), ('imperative', 1), ('getting', 1), ('fashions', 1), ('meditated', 1), ('cunning', 1), ('locomotives', 1), ('signed', 1), ('pampered', 1), ('wolfish', 1), ('ferocity', 1), ('preserver', 1), ('newcomers', 1), ('lash', 1), ('below', 1), ('splintering', 1), ('companies', 1), ('smiling', 1), ('ere', 1), ('imprisoned', 1), ('eye', 1), ('puzzled', 1), ('fat', 1), ('laws', 1), ('fed', 1), ('horribly', 1), ('fox', 1), ('ruction', 1), ('thirty', 1), ('exquisite', 1), ('stop', 1), ('lazy', 1), ('believing', 1), ('severe', 1), ('stable', 1), ('afternoon', 1), ('captain', 1), ('several', 1), ('straight', 1), ('teasing', 1), ('sure', 1), ('whistling', 1), ('kick', 1), ('frightful', 1), ('hot', 1), ('gone', 1), ('using', 1), ('told', 1), ('sounds', 1), ('northland', 1), ('developed', 1), ('slouch', 1), ('impending', 1), ('sensitive', 1), ('king', 1), ('likewise', 1), ('artesian', 1), ('rambles', 1), ('gambling', 1), ('bernard', 1), ('something', 1), ('pounded', 1), ('plunged', 1), ('sullenly', 1), ('lap', 1), ('fawned', 1), ('swift', 1), ('slower', 1), ('led', 1), ('treachery', 1), ('swing', 1), ('light', 1), ('lit', 1), ('torn', 1), ('prepared', 1), ('frost', 1), ('else', 1), ('town', 1), ('mad', 1), ('hidden', 1), ('may', 1), ('cure', 1), ('intolerable', 1), ('park', 1), ('mid', 1), ('part', 1), ('barrens', 1), ('bucked', 1), ('mud', 1), ('honestly', 1), ('lifeless', 1), ('windows', 1), ('solitary', 1), ('wheedlingly', 1), ('yelping', 1), ('flecked', 1), ('calm', 1), ('hurting', 1), ('makes', 1), ('treated', 1), ('camp', 1), ('foaming', 1), ('our', 1), ('demesne', 1), ('own', 1), ('wondered', 1), ('gloomy', 1), ('necessarily', 1), ('accepted', 1), ('oppressed', 1), ('pry', 1), ('gingerly', 1), ('taunted', 1), ('stables', 1), ('accompanied', 1), ('constantly', 1), ('goods', 1), ('jolted', 1), ('whatsoever', 1), ('loaded', 1), ('chops', 1), ('weary', 1), ('run', 1), ('inflammation', 1), ('ferry', 1), ('command', 1), ('crates', 1), ('hatred', 1), ('fetching', 1), ('linda', 1), ('sou', 1), ('tormentor', 1), ('sum', 1), ('endless', 1), ('caution', 1), ('nomadic', 1), ('sudden', 1), ('locomotive', 1), ('assailed', 1), ('coats', 1), ('sickly', 1), ('terms', 1), ('mother', 1), ('frothing', 1), ('populous', 1), ('dealt', 1), ('divined', 1), ('returning', 1), ('combined', 1), ('office', 1), ('surrounded', 1), ('menacingly', 1), ('panting', 1), ('downhill', 1), ('shifted', 1), ('wounded', 1), ('attracted', 1), ('bulging', 1), ('fountain', 1), ('mollie', 1), ('tail', 1), ('bolted', 1), ('health', 1), ('restrictions', 1), ('near', 1), ('traces', 1), ('scarlet', 1), ('growing', 1), ('won', 1), ('grappled', 1), ('mates', 1), ('scattering', 1), ('heels', 1), ('scale', 1), ('meeting', 1), ('wrenching', 1), ('library', 1), ('scatter', 1), ('yet', 1), ('suddenly', 1), ('rushing', 1), ('coolly', 1), ('demanded', 1), ('whale', 1), ('stroll', 1), ('favored', 1), ('civilization', 1), ('trick', 1), ('acquaintance', 1), ('tried', 1), ('helper', 1), ('promptly', 1), ('orchard', 1), ('hang', 1), ('coming', 1), ('opening', 1), ('concerning', 1), ('whirled', 1), ('price', 1), ('buckled', 1), ('twisted', 1), ('always', 1), ('finely', 1), ('parcels', 1), ('stormed', 1), ('bundled', 1), ('fall', 1), ('scene', 1), ('anxious', 1), ('wrestling', 1), ('none', 1), ('victim', 1), ('tireless', 1), ('ruled', 1), ('knocked', 1), ('action', 1), ('deliberately', 1), ('plant', 1), ('attempted', 1), ('lend', 1), ('parts', 1), ('parched', 1), ('exception', 1), ('start', 1), ('sufficient', 1), ('draught', 1), ('falling', 1), ('held', 1), ('survey', 1), ('help', 1), ('escorted', 1), ('swollen', 1), ('combatants', 1), ('buckles', 1), ('alert', 1), ('killed', 1), ('queen', 1), ('orchards', 1), ('release', 1), ('organizing', 1), ('scotch', 1), ('dropped', 1), ('want', 1), ('vilely', 1), ('letter', 1), ('angry', 1), ('clerks', 1), ('unkempt', 1), ('accumulated', 1), ('bodies', 1), ('alice', 1), ('arrive', 1), ('find', 1), ('pull', 1), ('kindred', 1), ('steal', 1), ('vi', 1), ('those', 1), ('aristocrat', 1), ('stern', 1), ('author', 1), ('high', 1), ('ebbed', 1), ('glance', 1), ('outreached', 1), ('hind', 1), ('flag', 1), ('outdoor', 1), ('santa', 1), ('wisdom', 1), ('licking', 1), ('large', 1), ('jerked', 1), ('crossing', 1), ('hated', 1), ('voice', 1), ('wife', 1), ('ankle', 1), ('boded', 1), ('depot', 1), ('will', 1), ('metallic', 1), ('shutting', 1), ('saloon', 1), ('mastery', 1), ('possessed', 1), ('considering', 1), ('gravelled', 1), ('fooled', 1), ('wrappings', 1), ('curiously', 1), ('shrewd', 1), ('driven', 1), ('blood', 1), ('change', 1), ('quarters', 1), ('side', 1), ('dimly', 1), ('limply', 1), ('therefore', 1), ('progeny', 1), ('score', 1), ('ryan', 1), ('savagely', 1), ('bone', 1), ('wintry', 1), ('clubbed', 1), ('hiding', 1), ('door', 1), ('hour', 1), ('madness', 1), ('tragic', 1), ('incurious', 1), ('exclamations', 1), ('hoarse', 1), ('lawns', 1), ('riding', 1), ('conciliated', 1), ('compared', 1), ('checked', 1), ('situation', 1), ('crashed', 1), ('candle', 1), ('enthusiastically', 1), ('handkerchief', 1), ('sounding', 1), ('progress', 1), ('gruffly', 1), ('character', 1), ('devil', 1), ('requires', 1), ('nipped', 1), ('allowed', 1), ('grunted', 1), ('mere', 1), ('ferine', 1), ('found', 1), ('stole', 1), ('beast', 1), ('athletic', 1), ('changed', 1), ('goose', 1), ('license', 1), ('despatches', 1), ('imagined', 1), ('store', 1), ('fastened', 1), ('plunge', 1), ('might', 1), ('nightmare', 1), ('apparent', 1), ('north', 1), ('easily', 1), ('tumbled', 1), ('twilight', 1), ('attempt', 1), ('spat', 1), ('demand', 1), ('spot', 1), ('remainder', 1), ('hauling', 1), ('newfoundland', 1), ('kinds', 1), ('pieces', 1), ('housemaids', 1), ('limb', 1), ('growling', 1), ('huge', 1), ('thinks', 1), ('glazed', 1), ('swart', 1), ('chinese', 1), ('placed', 1), ('hurt', 1), ('warning', 1), ('limp', 1), ('whole', 1), ('grimly', 1), ('onlooking', 1), ('slept', 1), ('frozen', 1), ('calmly', 1), ('interlacing', 1), ('regained', 1), ('latent', 1), ('races', 1), ('step', 1), ('scream', 1), ('vast', 1), ('southland', 1), ('living', 1), ('giant', 1), ('mexican', 1), ('damnation', 1), ('muscle', 1), ("you'll", 1), ('how', 1), ('justice', 1), ('iii', 1), ('filing', 1), ('shifting', 1), ('twist', 1), ('throbbed', 1), ('trampled', 1), ('flying', 1), ('stuff', 1), ('peered', 1), ('boughs', 1), ('leg', 1), ('lottery', 1), ('log', 1), ('crowed', 1), ('lolling', 1), ('nature', 1), ('literally', 1), ('charged', 1), ('dominant', 1), ('station', 1), ('mug', 1), ('fringed', 1), ('purposely', 1), ('described', 1), ('snarl', 1), ('whereupon', 1), ('expecting', 1), ('raged', 1), ('crumpled', 1), ('filled', 1), ('affection', 1), ('steamship', 1), ('bristled', 1), ('excitement', 1), ('raw', 1), ('demanding', 1), ('affirmative', 1), ('trucked', 1), ('sagged', 1), ('chinked', 1), ('sin', 1), ('footsteps', 1), ('name', 1), ('mushy', 1), ('ten', 1), ('whenever', 1), ('loved', 1), ('canadian', 1), ('top', 1), ('numerous', 1), ('enough', 1), ('firewood', 1), ('use', 1), ('steadily', 1), ('profit', 1), ('outrage', 1), ('st', 1), ('protect', 1), ('safe', 1), ('protest', 1), ('wot', 1), ('obscurely', 1), ('fever', 1), ('egotistical', 1), ('remarkable', 1), ('antagonist', 1), ('sometimes', 1), ('pastures', 1), ('helping', 1), ('intentness', 1), ('fighting', 1), ('imperiously', 1), ('silly', 1), ('speedily', 1), ('since', 1), ('entered', 1), ('pervaded', 1), ('weight', 1), ('promises', 1), ('wages', 1), ('deliver', 1), ('pulse', 1), ('waited', 1), ('guilty', 1), ('result', 1), ('weighed', 1), ('sprayed', 1), ('shriek', 1), ('sniffed', 1), ('daughters', 1), ('creeping', 1), ('clara', 1), ('minutes', 1), ('meant', 1), ('francisco', 1), ('leader', 1), ('sank', 1), ('lawgiver', 1), ('withheld', 1), ('beneath', 1), ('flapped', 1), ('encoding', 1), ('trifle', 1), ('further', 1), ('taught', 1), ('orderly', 1), ('lacerated', 1), ('clear', 1), ('crushingly', 1), ('anyone', 1), ('thus', 1), ('assailants', 1), ('whaling', 1), ('arbors', 1), ('culprit', 1), ('stalked', 1), ('joyful', 1), ('leashed', 1), ('ready', 1), ('tonic', 1), ('detestable', 1), ('wagged', 1), ('chance', 1), ('raised', 1), ('estimation', 1), ('fiercer', 1), ('receiving', 1), ('wrapped', 1), ('grape', 1), ('skyward', 1), ('brumal', 1), ('present', 1), ('david', 1), ('brass', 1), ('green', 1), ('groping', 1), ('laughing', 1), ('trembled', 1), ('forth', 1), ('raisin', 1), ('brutal', 1), ('online', 1), ('mentally', 1), ('flowing', 1), ('beach', 1), ('plainly', 1), ('cunningly', 1), ('calculated', 1), ('mind', 1), ('protected', 1), ('sort', 1), ('trouser', 1), ('destined', 1), ('futilely', 1), ('shook', 1), ('nursing', 1), ('consignment', 1), ('shepherd', 1), ('bad', 1), ('inseparable', 1), ('generously', 1), ('error', 1), ('struggled', 1), ('break', 1), ('displeasure', 1), ('savage', 1), ('treacherous', 1), ('travelled', 1), ('torment', 1), ('leaped', 1), ('got', 1), ('touch', 1), ('crossed', 1), ('lifted', 1), ('piece', 1), ('college', 1), ('smashed', 1), ('flash', 1), ('climbed', 1), ('peace', 1), ('removed', 1), ('beyond', 1), ('quoting', 1), ('revelation', 1), ('particularly', 1), ('small', 1), ('ahead', 1), ('backward', 1), ('poked', 1), ('armed', 1), ('pug', 1), ('interest', 1), ('choke', 1), ('remained', 1), ('swinging', 1), ('rage', 1), ('helpers', 1), ('repeatedly', 1), ('opened', 1), ('obeyed', 1), ('recover', 1), ('impartial', 1), ('grandsons', 1), ('date', 1), ('need', 1), ('passed', 1), ('surcharged', 1), ('follow', 1), ('downward', 1), ('surface', 1), ('railway', 1), ('insular', 1), ('dominion', 1), ('reaching', 1), ('assortment', 1), ('dave', 1), ('throttled', 1), ('rear', 1), ('excitedly', 1), ('metal', 1), ('announced', 1), ('should', 1), ('sang', 1), ('delights', 1), ('deathless', 1), ('weather', 1), ('virtue', 1), ('rest', 1), ('prompt', 1), ('clubs', 1), ('patted', 1), ('unexpected', 1), ('recovered', 1), ('cottages', 1), ('crawled', 1), ('camped', 1), ('atmosphere', 1), ('showed', 1), ('intimated', 1), ('poplars', 1), ('recesses', 1), ('calamity', 1), ('future', 1), ('fearlessly', 1), ('passing', 1), ('load', 1), ('colder', 1), ('eager', 1), ('wakens', 1), ('loaf', 1), ('growl', 1), ('broke', 1), ('my', 1), ('tallow', 1), ('certain', 1), ('morose', 1), ('chain', 1), ('mewed', 1), ('companion', 1), ('returned', 1), ('check', 1), ('rick', 1), ('chafing', 1), ('ride', 1), ('straps', 1), ('without', 1), ('selected', 1), ('treatment', 1), ('anywhere', 1), ('worth', 1), ('loser', 1), ('rise', 1), ('conveyance', 1), ('ship', 1), ('sides', 1), ('screaming', 1), ('tall', 1), ('rarely', 1), ('geological', 1), ('hardened', 1), ('perches', 1), ('doors', 1), ('conciliate', 1), ('underhand', 1), ('swimming', 1), ('shot', 1), ('master', 1), ('comes', 1), ('confusion', 1), ('ragged', 1), ('keeping', 1), ('wound', 1), ('slaver', 1), ('arms', 1), ('sorely', 1), ('succeeded', 1), ('barked', 1), ('cursing', 1), ('kidnapped', 1), ('senseless', 1), ('reproof', 1), ('desired', 1), ('klondike', 1), ('truck', 1), ('bends', 1), ('realized', 1), ('undid', 1), ('truly', 1), ('knee', 1), ('vicarious', 1), ('kennels', 1), ('road', 1), ('thrown', 1), ('trust', 1), ('humans', 1), ('roar', 1), ('genial', 1), ('thousand', 1), ('ropes', 1), ('longings', 1), ('deft', 1), ('mastership', 1), ('relax', 1), ('rows', 1), ('association', 1), ('shrieking', 1), ('nevertheless', 1), ('generous', 1), ('flagged', 1), ('peril', 1), ('standing', 1), ('fought', 1), ('enabled', 1), ('uncouth', 1), ('ignored', 1), ('resolved', 1), ('meat', 1), ('going', 1), ('savages', 1), ('show', 1), ('involuntarily', 1), ('uncowed', 1), ('bitter', 1), ('jerk', 1), ('fearful', 1), ('early', 1), ('ears', 1), ('outside', 1), ('thousands', 1), ('array', 1)]
        actual_output = self.frequency.ranking()

        actual_hashtable = LinearProbeHashTable(31, len(expected_output) * 2)
        for item in actual_output:
            actual_hashtable[item[0]] = item[1]

        # Test all frequencies are correct and check the top 10 most common words
        count = 0
        for expected_item in expected_output:
            expected_word, expected_word_frequency = expected_item
            try:
                self.assertEqual(expected_word_frequency, actual_hashtable[expected_word])
            except KeyError:
                raise AssertionError("{} not found".format(expected_word))
            else:
                if count < 10:
                    self.assertEqual(expected_item, actual_output[count])
                count += 1

        # TODO: Add 2 or more unit tests
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()

