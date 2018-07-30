from unittest.case import TestCase

from html2json import chhue
from bs4 import BeautifulSoup


class chhigiam(TestCase):
    def test_2260(self):
        chu = list(chhue(BeautifulSoup(self.artical2260, 'lxml')))
        self.assertEqual(
            chu[:2], ['Ia̍p Tsùn ê Sió-toān.', '1916.04 373 koàn p.6']
        )

    def test_2263(self):
        chu = list(chhue(BeautifulSoup(self.artical2263, 'lxml')))
        self.assertEqual(chu[:2], ['Sin-iok Thâu-sū.', '(Pa Khek-lé kì).'])

    artical2260 = '''<span class="gy12"><p>Ia̍p Tsùn ê Sió-toān.<br />1916.04 373 koàn p.6<br />Ia̍p Tsùn chhut-sì tī Tsú-āu 1867 nî. Tis7oe-hàn ê sî pē-bú sàn-hiong, ū tha̍k tām-po̍h Hàn-o̍h nā-tiāⁿ, chiū hō͘ lâng chhiàⁿ choè sin-lô. I ê tē sì hiaⁿ tāi-seng tit-tio̍h tō-lí, i chiū chīn la̍t chó͘-tòng, chóng-sī bô kú i ê tē sì hiaⁿ ū khì Tām-suí ji̍p Sîn-ha̍k-hāu. āu-lâi in lāu-bú ū phoà-pīⁿ khì Tām-suí chhē i-seng. Iapch8un chiū khì chiàu-kò͘, tuì án-ni chiū tit-tio̍h tō-lí. Tuì 16 hè khí chiū khì kun-suî Lē Bo̍k-su, 17 hè nî-bé chiuj7...p Sîn-ha̍k, 21 hè chiū chhut-lâi chuí-tńg-kha choè Thoân-tō. Hit-sî i ū chīn la̍t kó͘-bú kàu-hoē kap kó͘-bú khí sin pài-tn̂g. Tuì án-ni kàu-hoē chiū chiām-chiām heng-khí. Tuì Tè-kok léng Tâi ê sî, i ū pī-lān poaⁿ khì Tām-suí pài-tn̂g. āu-lâi ū beh kā i choán-jīm, in-uī ū kuí-nā hāng ê chó͘-tòng, chiū sichit5 hioh kang, iû-goân koh tiàm chuí-tńg-kha choè seng-lí kap choè i-seng. <br />Taⁿ hioh kang liáu-āu ū thang pang-chān kàu-hoē ê só͘-chāi, i chin hoaⁿ-hich2oe, iā chhut-la̍t toê-iân choè kàu-hoēe bô͘-iūⁿ. Put-hēng tī kū-nî bé ū phoà-pīⁿ ji̍p Má-kai i-īⁿ; tāi-seng tit-tio̍h i-seng chīn la̍t i-tī, pīⁿ chiām-chiām khah hó. In-uī seng-lí kap lâng tn̂g-té ê susīuN tio̍h ko͘-put-chiong chhut īⁿ tò-tńg lâi, pīⁿ-sè koh tú-tio̍h ná siong-tiōng. Kàu pún nî 2 ge̍h 7 hō koh ji̍p īⁿ, chóng-sī khó-sioh chia̍h io̍h bô hāu, tī 2 ge̍h 18 hō hō͘ chú kéng-tiàu lī-khui sè-kan,kè ji̍t soà tī hia bâi-chòng. Ū tit-tio̍h kuí-nā uī se-kok kap pún-toē Bo̍k-su,Thoân-tō-su, Sîn-ha̍k-hāu ê ha̍k-seng kap Toā-tiū-tiâⁿ, Báng-kah, chuí-tńg-kha ê kàu-hoē lâi sàng-chòng, tì-ì ài siá kuí-jik7a lia̍t-uī seh-siā. Taⁿ kàu-hoē ū sit-lo̍h chi̍t ê jia̍t-sim ê hoē-iú, i ê bó͘-kiáⁿ ū si̍t-lo̍h chi̍t ê thâu-chàng, kiám m̄ siong-pi mah.?<br />(Ia̍p Kim-bo̍k kì.)</p></span>'''

    artical2263 = '''<span class="gy12"><p>Sin-iok Thâu-sū.</p>
<p>(Pa Khek-lé kì).</p>
<p>1916. 4, no. 373, pp. 8-9</p>
<p>&nbsp; Sì-tsa̍p goā nî chêng ū chiong Sin-iok hoan-e̍k pe̍h-oē-jī. Hit-tia̍p kàu taⁿ ū boē kuí-nā chheng pún, hō͘ chin tsoē lâng tha̍k, lâi tit-tio̍h toā lī-ek; sī in-uī ta̍k lâng thang ka-kī káng-kiù Siōng-tè ê Sèng-chheh.</p>
<p>&nbsp; Jī saⁿ tsa̍p nî í-lâi ū joā tsoē lâng teh phah-sǹg chêng só͘ hoan-e̍k--ê tio̍h koh-tsài chim-chiok, hō͘ i khah tsún, thang tú-tú chiàu pún-bûn ê ì-sù. In-uī pún só͘ hoan-e̍k--ê khiok sī Sèng-keng tāi-khài ê ì-sù lóng chiâu tī-teh: tsóng-sī hit pún ê pe̍h-oē, í-ki̍p hit pái só͘ ēng lâi koé-seh ê Hàn-bûn, bô thang hō͘ tha̍k ê lâng siông-siông tsai tù-chheh ê lâng ê ì-sù kàu tsún-tsún.</p>
<p>&nbsp; Só͘-í kūn-lâi ū chhiáⁿ sì ê Sian-siⁿ tuì Hi-lī-nî ê pún-bûn têng-tsài hoan-e̍k, koh ū chiong sin hoan-e̍k ê Hàn-bûn la̍k chhit pún lâi saⁿ chham khoàⁿ. Kàu hoan-e̍k liáu, chiū pun hō͘ kuí-nā uī ê Sian-siⁿ chham-kàu; chiah koh-tsài chim-chiok sûn chi̍t nn̄g piàn. Thâu kàu bé ēng kang nn̄g nî khah ke. Taⁿ hoat-hêng tsoè Kàu-hoē ê lō͘-ēng.</p>
<p>&nbsp; Soà pâi-lia̍t kuí-nā hāng tī ē-toé, hō͘ lâng khah tsai-iáⁿ tha̍k.</p>
<p>&nbsp; 1. Chheh-tiong ū-sî ēng chhiâ-jī. Che sī pún-bûn tī hit tsat bô hit ê jī, iáu-kú ū hit ê ì-sù; só͘-í goán thiⁿ hit jī hō͘ i khah chiâⁿ kù. (Khoàⁿ Hēng-toān 13:25, "Goá m̄ sī <em>Ki-tok</em>"; pún-bûn kan-ta siá, "Goá m̄ sī"; "Ki-tok" nn̄g-jī sī goán thiⁿ-ê.)</p>
<p>&nbsp; 2. Ū só͘-tsāi goán ēng tsù-kha, hit ê in-toaⁿ ū kuí-nā-hāng:-</p>
<p>&nbsp; (1) Pún-bûn ê jī ū só͘-tsāi thang hoan-e̍k kuí-nā iūⁿ ê ì-sù, lâng só͘ phah-sǹg bô lóng saⁿ-tâng. Goán chiū kéng só͘ khoàⁿ-tsoè khah tio̍h-ê, lâi hoan-e̍k tsoè chiàⁿ bûn; ēng pa̍t-iūⁿ ê ì-sù kì tsoè tsù-kha. (Thang khoàⁿ I Ko-lîm-to 7:21; Hi-pek-lâi 2:18.)</p>
<p>&nbsp; (2) Kó͘-tsá ê sî lâng boē hiáu-tit ìn chheh ê hoat-tō͘; só͘ ū ê chheh sī ēng chhiú siá-ê. Sèng-chheh chhau-siá ê kó͘-bûn ū só͘-tsāi sió-khoá cheng-choa̍h, tì-kàu Sian-siⁿ boē-oē koat-toàn goân-bûn ê jī tú-tú sī tī tá-lo̍h chi̍t-ê. Goán chiū ēng só͘ khoàⁿ-tsoè khah tsún-ê lâi tsoè bûn: kî-û--ê tsoè tsù-kha. Kî-si̍t só͘ cheng-chha--ê lóng bô gāi-tio̍h iàu-kín ê tō-lí.</p>
<p>&nbsp; (3) Ū só͘-tsāi nā beh chiàu pún-bûn ê oē jī-jī lâi hoan-e̍k, kiaⁿ-liáu hiah ê oē khah kan-kè tha̍k; goán chiū ēng khah pe̍h ê oē tsoè bûn, ēng khah tsún ê ì-sù tsoè tsù-kha. (Thang khoàⁿ Iok-hān 2:17, Hui-lī-bûn 16 tsat.)</p>
<p>&nbsp; (4) Nā ū ín Kū-iok ê oē, goán chiū chiong hit ê chiuⁿ-tsat kì tsoè tsù-kha.</p>
<p>&nbsp; Chiah ê tsù-kha sī teh tsoè káng-kiù Sèng-chheh ê lō͘-ēng; lâng tha̍k Sèng-chheh ê sî thang chiàu toā-bûn ti̍t-ti̍t tha̍k-khì chiū hó.</p>
<p>&nbsp; 3. Chheh-tiong só͘ ū ê "<em>I</em>"--jī, nā sī chí Siōng-tè, chiū lóng ēng toā-pún ê jī. Só͘ ū ê "<em>Sîn"</em>--jī iā sī án-ni. Pún-bûn khiok bô hun-piat toā sió pún; goán sī chiàu só͘ káng-kiù lâi gī-tiāⁿ. Ta̍k lâng thang ka-kī phah-sǹg.</p>
<p>&nbsp; "<em>Goán"</em>--jī kap "<em>lán"</em>--jī, pún-bûn sī tâng chi̍t jī, iû-goân sī hoan-e̍k ê sî chiàu só͘ káng-kiù lâi gī-tiāⁿ. Tha̍k ê lâng iā thang ka-kī phah-sǹg. (Thang khoàⁿ Ka-lia̍p-thài 2:15).</p>
<p>&nbsp; 4. Ū-sî só͘ ín Kū-iok ê oē pâi tsoè té-tsoā; che sī in-uī pún-bûn sī chhin-chhiūⁿ si ê khoán.</p>
<p>&nbsp; 5. Ū kuí-nā kù siông-siông ēng ê oē, goán hoan-e̍k ê sî ū sió-khoá oāⁿ, hō͘ i khah ha̍p chit pêng ê lō͘-ēng. Taⁿ pâi-lia̍t tī-chia, chiū chheh-lāi m̄-bián ta̍k pái tsù-bêng.</p>
<p>&nbsp;&nbsp;&nbsp; boē Iâ-so͘, <em>pún-bûn </em>chiong Iâ-so͘ kau-hù.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; toā-pêng , ; ; chiàⁿ-chhiúⁿ-pêng.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; goā-pang, ; ;&nbsp; lia̍t-pang.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; Kiù-tsú, ; ;&nbsp;&nbsp; Kiù-chiá.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; sèng-tô͘, ; ;&nbsp; sèng ê.</p>
<p>&nbsp; &nbsp;&nbsp;&nbsp;koh-oa̍h, ; ;&nbsp;&nbsp; koh khí-lâi.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; thiⁿ-sài, ; ;&nbsp;&nbsp;&nbsp; sù-chiá. Chit jī ū só͘-tsāi sī chí lâng á-sī kuí; goán chiū hoan-e̍k tsoè "<em>sù-chiá"</em>. (Thang khoàⁿ Má-thài 11:10, 5:41.)</p>
<p>&nbsp; Ū chi̍t jī kì tī Sin-iok chha-put-to 150 pái, i-ê ì-sù pún-jiân sī "<em>bah</em>". <em>(Khoàⁿ Lō͘-ka 24:39, Khé-sī-lio̍k 19:18). </em>Tsóng-sī hit jī ū pau-hâm khah tsoē hāng ê ì-sù. Chêng teh ēng pe̍h-oē ê Sin-iok ū hoan-e̍k tsoē-tsoē hāng ê jī, chhin-chhiūⁿ ē-bīn só͘ kì-ê: <em>thé (Má-thài 19:6), lâng (Má-thài 24:22), seng-khu (Má-thài 26:41), ū hiat-khì--ê (Lō͘-ka 3:6), chêng-io̍k (Iok-hān 1:13), goā-phê (Iok-hān 8:15), peh-sìⁿ (Iok-hān 17:2), su-io̍k (Lô-má 8:6), kut-jio̍k (Lô-má 9:3), goā-māu (I Ko-lîm-to 1:26), sai-khia ê ì-sù (II Ko-lîm-to 1:17), ū hêng (II Ko-lîm-to 1:17), ū hêng (II Ko-lîm-to 7:1), lâng ê hoat-tō͘ (Ka-lia̍p-thài 4:23), tso̍k-luī (Í-hut-só͘ 2:11), só͘ ho̍k-sāi (Í-hut-só͘ 6:5), sè-kan (Hui-li̍p-pí 1:22), pún-sin (Ko-lô-se 1:22), tiàm tī sè-kan (Hi-pek-lâi 5:7), sek (Iû-tāi 7 tsat).</em> Chiàu goán phah-sǹg, nā oē-tit thang ēng tiāⁿ-tio̍h ê jī lâi hoan-e̍k sī khah hó, só͘-í khah siông hoan-e̍k tsoè "<em>jio̍k-thé"</em>. Tha̍k ê lâng thang tsai chit jī pún-bûn sī bah, iā tio̍h chiàu téng ê bûn ê ì-sù lâi koé-seh.</p>
<p>&nbsp; Koh ū chi̍t kù, "<em>tī Ki-tok</em>", iā sī Sin-iok tiong siông-siông ū-ê, Pó-lô ê phoe tē it tsoē. Chêng só͘ ēng ê Sin-iok ū chiong chit jī hoan-e̍k tsoē-tsoē hāng, chhin-chhiūⁿ ē-bīn só͘ kì-ê:<em> sio-liân (Iok-hān 15:4), ha̍p tī (Iok-hān 17:23), chiong (Hēng-toān 17:31), khò (Lô-má 6:11), tī (Lô-má 8:1), jīn tsoè Chú (Lô-má 9:1), sio̍k (Lô-má 16:3), in-uī (I Ko-lîm-to 1:4), thok-tiōng (II Ko-lîm-to 5:19), tuì (Ka-lia̍p-thài 3:14), ēng (Í-hut-só͘ 2:10), kì-liām (II Thê-mô͘-thài 1:9), thàn (Hui-lī-bûn 20 tsat), kau-poê (I Iok-hān 4:15). </em>Tsóng-sī chit kù ū chhim ê ì-sù, só͘-í goán ū hoan-e̍k tsoè "<em>tiàm tī Ki-tok</em>". Nā-sī pō͘-pîn tha̍k ê sî, thiaⁿ-liáu khah m̄ koàiⁿ-sì, lâng m̄ thang khì-hiâm, tio̍h káng-kiù hit ê khah chhim ê ì-sù.</p>
<p>&nbsp; iā ū chi̍t jī, ì-sù sī "<em>lí khoàⁿ"</em>, Sin-iok tiong chha-put-to 200 pái. Goán ū-sî sī chiàu án-ni hoan-e̍k, ū-sî hoan-e̍k "<em>hut-jiân"</em> á-sī "<em>tú-tn̄g"</em>; tsóng-sī khah-siông sī lóng bô hoan-e̍k.</p>
<p>&nbsp; Sin hoan-e̍k Hàn-bûn ê Sèng-chheh ū ēng "<em>be̍k-sī"</em> oāⁿ tsoè "<em>khé-sī"</em>; goán khoàⁿ hit-ê sī khah ha̍p, só͘-í ū thàn i. Taⁿ Sin-iok ê lō͘-bé pún ū oāⁿ i ê miâ tsoè "<em>Khé-sī-lio̍k"</em>.</p>
<p>&nbsp; 6. Lâng tha̍k kū hoan-e̍k--ê koàiⁿ-sì, pō͘-pîn tha̍k chit pún sin-ê, chhin-chhiūⁿ khah oh bêng; che iā bo̍k-koài. In-uī Sèng-chheh tsoē-tsoē só͘-tsāi ì-sù chin-chhim, boē tit thang chi̍t-ē khoàⁿ chiū thàu-thiat. Chêng só͘ hoan-e̍k--ê sī thé-thiap lâng ê kan-kè bêng, chiū tī tsoē-tsoē só͘-tsāi ū hoan-e̍k khah khín, pí pún-bûn iáu khah bêng (thang khoàⁿ Hui-li̍p-pí 3:12). Goán bô án-ni; sī ài ēng tsá-sî tù-chheh ê lâng só͘ siá Hi-lia̍p ê bûn oāⁿ tsoè pún-toē ê pe̍h-oē, hō͘ tha̍k ê lâng oán-jiân chhin-chhiūⁿ tsāi-tsá ê Kàu-hoē teh tha̍k pún-bûn chi̍t-iūⁿ. Lâng thâu-piàn teh tha̍k oē tit-tio̍h lī-ek, tsóng-sī bô thang lóng bêng-pe̍k; to̍k-to̍k tio̍h tsài-saⁿ káng-kiù, tì-ì kî-tó, chiū ná kú ná bêng, só͘ tit-tio̍h ê kà-sī m̄-sī chiàu lâng ê ì-sù, sī tú-tú tit-tio̍h Sèng-chheh si̍t-tsāi ê ì-sù.</p>
<p>&nbsp; Chit-pún Sèng-chheh goân-pún sī chhut tī Sèng-sîn ê khé-sī: taⁿ kiû I chiàu I ê un-tián lâi ín-chhoā tha̍k ê lâng, hō͘ in khûn-khûn káng-kiù, thang ná kú ná tsai Siōng-tè tiàu lán tsoè I ê peh-sìⁿ ū sím-mi̍h hok-khì thang ǹg-bāng, iā tit-tio̍h tsai Ki-tok boē chhek-to̍k-tit ê pù-ū.</p>
<p>A-bēng.</p></span>'''
