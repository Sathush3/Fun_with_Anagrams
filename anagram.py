def anagram(text1, textArray):
    for i in textArray:
        if sorted(text1) == sorted(i):
            return True
    return False


def funWithAnagrams(text):
    text.reverse()
    final_text = list(text)
    for i in range(len(text) - 1):
        if anagram(text[i], text[i + 1:]):
            final_text.pop(0)
    return (sorted(final_text))


print(funWithAnagrams(['code', 'doce', 'ecod', 'framer', 'frame']))
print(funWithAnagrams(['poke', 'pkoe', 'okpe', 'ekop']))
print(funWithAnagrams(['fqwltvzkqt', 'volphckcyufdqmlglimklfzktgygdttnhcvpfdfbrp', 'lkvshwywshtdgmbqbkkxcvgumo',
  'mwvytbytnuqhmfjaqtgngcwkuzyamnerphfmwevh', 'lezohyeehbrcewjxvceziftiqtntfsrptugtiznorvonzjfea',
  'gamayapwlmbzitzszhzkosvnknber', 'ltlkggdgpljfisyltmmfvhybljvk', 'pcflsaqevcijcyrgmqirzniax',
  'kholawoydvchveigttxwpukzjfh', 'brtspfttotafsngqvoijxuvq', 'ztvaalsehzxbshnrvbykjqlrzzfm',
  'vyoshiktodnsjjpqplciklzqrxloqxrudygjty', 'leizmeainxslwhhjwslqendjvx', 'yghrveuvphknqtsdtwxcktmwwwsdthzmlmbh',
  'kmouhpbqur', 'fxgqlojmwsomowsjvpvhznbsilhhdkbdxqgrgedpzch', 'gefeukmcowoeznwhpiiduxdnnlbnmyjyssbsococdzcu',
  'nkrfduvouaghhcyvmlkza', 'jpfpyljtyjjpyntsefxiswjuten', 'ycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvguxtrdsdf',
  'fssmeluodjgdgzfmrazvndtaur', 'kugs', 'dpawxitivdubbqeonycaegxfjkkl', 'fkraoheucsvpiteqrs',
  'gkaaaohxxzhqjtkqaqhkwbe', 'bpmglbjipnujywogwc', 'lkyrdejaqufowbigrsnjniegvd',
  'otugocedktcbbufnxorixibbdfrzuqsyrfqghoyqevcuanuu', 'szitaoaowsxyglafbwzddoznrvjqeyqignpi',
  'ruijvyllsibobjltusrypanvybsfrxtlfmpdidtyozoolz', 'lgdgowijatklvjzscizrkupmsoxftumyxifyunxucubvk', 'ctkqlr',
  'qgzjvjwzizppvso', 'flvioemycnphf', 'tbnwedtubynsbirepgcxfgsfomhvpmymkdoh', 'ttyyc', 'ibbeaxniwjkfvabnrll',
  'maglythkgla', 'zgkeulyrpaeurdvexqlwgakdtbihmfrjijanxkhrqdllecy', 'pcflsaqevcijcyrgmqixnzira', 'klqrct',
  'ibbeaxniwjkfvanrbll', 'vyoshiktodnsjjpqplciklzqrxloqxrudyyjtg',
  'ycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvgxddftsru', 'yyctt', 'yghrveuvphknqtsdtwxcktmwwwsdtlhbhmmz',
  'vyoshiktodnsjjpqplciklzqrxloqxrugyytjd', 'cttyy', 'brtspfttotafsngqvoiqxuvj', 'lkyrdejaqufowbigrsnjvedgin',
  'volphckcyufdqmlglimklfzktgygdttnhcvpfdrbpf', 'qgzjvjwzizpsovp'
]))
