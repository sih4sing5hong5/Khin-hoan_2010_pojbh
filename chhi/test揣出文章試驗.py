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

    def test_10004(self):
        chu = list(chhue(BeautifulSoup(self.artical10004, 'lxml')))
        self.assertEqual(
            chu[10],
            '1. Tī siâⁿ-goā. Iok-hān 19:17 kóng, "Iâ-so͘ giâ ka-kī ê si̍p-jī-kè chhut-khì kàu chi̍t ê miâ kiò Thâu-khak-oáⁿ ê só͘-chāi, Hi-pek-lâi ê oē kiò-choè Kok-kok-thaⁿ."Hi-pek-lâi 13:12 kóng, "Iâ-so͘ in-uī beh ēng ka-kī ê hoeh hō͘ peh-sèⁿ chiâⁿ-sèng, ia̍h siū-khó͘ tī siâⁿ-mn̂g goā."'
        )

    def test_99(self):
        chu = list(chhue(BeautifulSoup(self.artical99, 'lxml')))
        self.assertEqual(
            chu[-1],
            '佮伊無閣相離。'
        )

    def test_11905(self):
        chu = list(chhue(BeautifulSoup(self.artical11905, 'lxml')))
        self.assertIn(
            '1. Lán tio̍h gâu ēng sìn-gióng ê kng kap te̍k-koân.',
            chu
        )

    def test_12045(self):
        chu = list(chhue(BeautifulSoup(self.artical12045, 'lxml')))
        self.assertEqual(
            chu[0],
            'Sin Thé-chè ê Kàu-hoē'
        )
    artical12045 = '''<span class="gy12"><p><!--[if gte mso 9]><xml> Normal   0      0   2      false   false   false                                                         MicrosoftInternetExplorer4 </xml><![endif]--><!--[if gte mso 9]><xml> </xml><![endif]--><!--[if !mso]> 
<object  classid="clsid:38481807-CA0E-42D2-BF39-B33AF135CC4D" id=ieoo͘i>
</object>
<style>
st1\:*{behavior:url(#ieoo͘i) }
</style>
<![endif]--> <!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoⁿormalTable
    {mso-style-name:表格內文;
    mso-tstyle-rowband-size:0;
    mso-tstyle-colband-size:0;
    mso-style-noshow:yes;
    mso-style-parent:"";
    mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
    mso-para-margin:0cm;
    mso-para-margin-bottom:.0001pt;
    mso-pagination:widow-orphan;
    font-size:10.0pt;
    font-family:"Times New Roman";
    mso-fareast-font-family:"Times New Roman";
    mso-ansi-language:#0400;
    mso-fareast-language:#0400;
    mso-bidi-language:#0400;}
</style>
<![endif]--></p>
<p>Sin Thé-chè ê Kàu-hoē</p>
<p>Phoaⁿ Tō-êng</p>
<p>1941年4月673期&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 17-19</p>
<p>&nbsp;</p>
<p>&nbsp; Nā beh ta̍t-sêng Sin thé-chè ê bo̍k-tek, m̄-sī kan-ta ū goā-pō͘-tek ê ki-kò͘(機構) kap chhiú-toāⁿ; tē-it iàu-kín sī kok-bîn ta̍k lâng ê lêng-hûn tio̍h tiàm tī Ki-tok choè sin chhòng-chō--ê; só͘-í hiān-tāi chong-kàu-kài ê chek-jīm sī chin tiōng-tāi. Ki-tok-kàu eng-kai chek-èng sin thé-chè, chiâⁿ-choè Sin Thé-chè ê Kàu-hoē . Sím-mi̍h sī Sin Thé-chè ê kàu-hoē?</p>
<p>&nbsp; 1.<em> Khoe-ho̍k(</em><em>恢復</em><em>) Ū-giân-chiá ê cheng-sîn.</em></p>
<p>&nbsp; Kū-iok ê chong-kàu ū nn̄g ê tiau-liû, chiū-sī Chè-si-tek ê chong-kàu kap Ū-giân-chiá w4 chong-kàu. Chiân-chiá, sī tuì-tiōng hêng-sek; hō͘-chiá, sī iàu-kín loē-iông. In-uī tng-sî soán-bîn chí-ū ēng goā-phê teh pài Siōng-tè ; só͘-í Sian-ti A-mô͘-sū chiū kéng-kò in kóng, "Lín sui-jiân hiàn sio chè, Goá bô hoaⁿ-hí ; hiàn puî ê cheng-siⁿ , Goá bô beh kàm-la̍p"(A-mô͘-sū 5:22-24).</p>
<p>&nbsp; Ki-tok-kàu sī si̍t-chián(實踐) ê chong-kàu . Chú Iâ-so͘ ū kóng, Lín ê gī bô iâⁿ-kè keng-ha̍k-sū kap Hoat-lī-sài lâng ê gī, koat-toàn boē-tit ji̍p Thian-kok(Má-thài 5:20).</p>
<p>&nbsp; リンドバーク tāi-chò só͘ hoat-piáu "<em>Bē-lâi ê toā hái-éng"</em> hit phiⁿ lūn-bûn ū chi̍t chām án-ni kóng: "BÍ-kok in pún-sin chū-sìn sī chèng-gī ê kok, Bí-kok tuì sè-kài ê chú-tiuⁿ sī choa̍t-tuì; lâng nā hoán-tuì, chiū-sī Mô͘-kuí. Che ū tú-tú tio̍h bô? Sèng-keng só͘ kì hit ê hó-gia̍h chheng-liân, tuì Chú Iâ-so͘ mn̄g kóng, Goá tio̍h cháiⁿ-iūⁿ choè, chiah thang sêng-chiap éng-oa̍h? Ki-tok ìn kóng, Lí ū iú-hàu bô? Lí ū thiàⁿ chhù-piⁿ bô?" Lí ū kèng Siōng-tè bô?Chheng-liân ìn kóng. Ū. Choè-āu Ki-tok kā i kóng. Lí iáu khiàm chi̍t hāng, tio̍h khì boē lí hoān só͘-ū--ê, lâi hō͘ sàn-hiong lâng, koh lâi tè Goá. Hit ê chheng-liân sit-sek, iu-būn chiū khì. Chit ê kò͘-sū tio̍h chhim-siūⁿ--i. Bí-kok chū-sìn in ū chhut-la̍t tī sè-kài ê pêng-hô; koat-toàn tuì sè-kài bô ū choè siáⁿ m̄ tú-hó tī-teh. Chóng-sī tio̍h chai, Ki-tok iā beh choè-āu án-ni tuì Bí-kok kóng, Lí iáu khiàm chi̍t hāng. Só͘ khiàm chit hāng, sī hiān-tāi chai-hō ê goân-thâu."</p>
<p>&nbsp; Phí-jîn ín i ê oē , ài lán hiān-tāi kàu-hoē tio̍h ka-kī hoán-séng. Kiaⁿ-liáu lán bô teh si̍t-hêng kài-bēng ê chin-chhoé, chiū-sī Thiàⁿ chhù-piⁿ chhin-chhiūⁿ ka-kī.</p>
<p><em>&nbsp; 2. Ko-tiāu(</em><em>高調</em><em>) Ki-tok-kàu kò͘-iú (</em><em>個有</em><em>) ê cheng-sîn:</em></p>
<p>&nbsp; Sī sím-mi̍h? Chiū-sī chin ê oa̍h-miā Ki-tok kóng, Goá sī oa̍h-miā. Chit ê oa̍h-miā sī èng sî-tāi ê iau-kiû. Ki-tok-kàu tī Lô-má kok 300 nî kú, siū pek-hāi, ū táⁿ-phoà Lô-má tè-kok chú-gī, kiàn-siat chin ê Kàu-hoē . Ki-tok kóng, Thian-kok chhin-chhiūⁿ <em>Kàⁿ</em> , chhin-chhiūⁿ <em>Koà-chhài-chí</em>; in-uī ū kái-chō kap hoat-tián ê oa̍h-miā la̍t tī-teh. Ki-tok-kàu sī oa̍h-miā ê chong-kàu. Bô ū Ki-tok ê Sîn--ê(oa̍h-miā), m̄-sī Ki-tok ê Kàu-hoē (Lô-má 8:9). Oāⁿ oē lâi kóng, M̄-sī sin thé-chè ê kàu-hoē.</p>
<p><em>&nbsp; 3. Soat-sin Ji̍t-iāu Ha̍k-hāu ê kàu-io̍k.</em></p>
<p>&nbsp; ēng Kok-gú lâi thoè Pe̍h-oē-jī ê kàu-siū, che sī èng sî-tāi ê iau-kiû. Chóng-sī tio̍h chai , Ji̍t-iāu ha̍k-hāu ê kàu-io̍k, chiū-sī ēng Siōng-tè kok choè bo̍k-phiau, Siōng-tè ê Thiàⁿ ê kàu-io̍k. Oāⁿ oē lâi kóng, chiū-sī Hok-im chú-gī ê chong-kàu kàu-io̍k. Hō͘ ta̍k ê ha̍k-seng chiong-lâi chiâⁿ-choè hó ê Ki-tok-tô͘, hó ê kok-bîn. Ji̍t-iāu ha̍k-hāu ê sêng-kong, sī chāi tī ū tú-hó ê kàu-oân. Ū lâng kóng, chāi-lâi ê kàu-oân khiàm jia̍t-sim kap hèng-bī. ǹg-bāng hiān-tāi ê kàu-oân ka-kī hoán-séng, soà put-sî gâu kap ha̍k-seng kau-poê, hō͘ in chiâⁿ-choè sìn-gióng sin thé-chè ê Ki-tok-tô͘; chiah bô ko͘-hū Siōng-tè ê kau-thok.</p>
<p>&nbsp; Chhú-khì só͘ beh sêng-li̍p ê Kok-bîn Ha̍k-hāu ê kàu-io̍k kun-pún hong-chiam chiū-sī tû-khì chāi-lâi siāng chi̍t khoán ki-hâi-tek ê kàu-io̍k, koh kiàn-siat gī-sio̍k kàu-io̍k ê cheng-sîn. Hit ê bo̍k-tek, chiū-sī Hông-bîn ê liān-sêng(皇民ノ煉成) . Chet hang choè lán chin toā ê chham-khó.</p>
<p><em>&nbsp;</em><em>&nbsp;4. Oân-sêng Ki-tok ê lí sióng.</em></p>
<p>&nbsp; Ki-tok só͘ lí-sióng ê kàu-hoē, sī sin thé-chè ê kàu-hoē . Siáⁿ khoán? Chhiáⁿ khoàⁿ Ngá-ko 6:10 ū kóng, Tù-hiān chhin-chhiūⁿ chá-khí-sî ê kng; suí chhin-chhiūⁿ ge̍h; chheng-kiat chhin-chhiūⁿ ji̍t; ui-gî chhin-chhiūⁿ kia̍h toā-kî ê kun-tuī--ê. Chóng kóng, chiū-sī ū Sèng-chheh-tek ê sìn-gióng ; ū Thiàⁿ; ū Sèng-kiat ; koh ū it-tì thoân-kiat ióng-kám tī-teh.</p>
<p><em>&nbsp; 5. Tui-kiû sin thé-chè ê chin cheng-sîn.</em></p>
<p><em>&nbsp; Bia̍t-su hōng-kong ,</em> che sī kin-ná-ji̍t lán Tè-kok só͘ kiông-tiau--ê. Chóng-sī Ki-tok tī nn̄g chheng nî chêng í-keng kà-sī liáu lah. Ki-tok ū kóng, Lín tio̍h kiû Siōng-tè ê Kok kap I ê Gī. M̄-sī kiû an-ia̍t, bêng-lí êng ta̍t choè tē-it, chiū-sī kiàn-siat sè-kài sin tia̍t-sū pêng-hô ê ông-kok choè tē-it.</p>
<p>&nbsp; Ki-tok-tô͘ loā-choē kam-goān chiong i ê châi-sán 10 hun chi̍t hiàn hō͘ Siōng-tè ah? Tio̍h lia̍h kàu-hoē choè tē-it, kàu-hoē tio̍h oân-choân chū-kip.</p>
<p>&nbsp;<em>&nbsp;6. Hoat-hui Kàu-hoē ê tiong-sim sù-bēng.</em></p>
<p>&nbsp;<em>&nbsp;Tuì lāi</em>: (1) Chip-siú Sèng lé-tián(Soé-lé kap Boán-chhan); (2) Kèng-pài Thiⁿ Pē;(3) Hùn-liān hoē-iú.</p>
<p>&nbsp;<em>&nbsp;Tuì goā</em>: (1) Thoân Hok-im; (2) Kiàn-siat chû-siān ê sū-gia̍p(Iâ-so͘ sì-koè kiâⁿ, choè hó-sū) uī-tio̍h kok-ka siā-hoē tô͘-bô͘ hēng-hok--ê, chiah thang ke-thiⁿ jîn-seng ê hēng-hok.</p>
<p><em>&nbsp; </em><em>7. Pò-chhî káng-toâⁿ ê koân-ui.</em></p>
<p>&nbsp; Chú Iâ-so͘ tuì káng-toâⁿ lo̍h-lâi ê sî, chèng-lâng kî-koài I ê kà-sī. In-uī I kà-sī lâng ū koân-lêng tī-teh. Hit ê koân-lêng(ū la̍t thang kám-tōng lâng), chiū-sī I 30 nî kú chún-pī ê kî-kan só͘ tit-tio̍h ê lêng-le̍k.</p>
<p>&nbsp; Ha̍k-chiá kóng. Hē-thiⁿ teh háu ê siân-á, i tī thô͘-lāi ê seng-oa̍h tio̍h 9 nî á 12 nî kú, chiah oē thang án-ni . Kin-á-ji̍t ê thoân-kàu-chiá 4 nî á 5 nî ê chún-pī, chiū it-seng-gâi teh thoân-tō, bo̍k-koài i só͘ khiā hit ê káng-tâi bô koân-ui tī-teh.</p>
<p>&nbsp; Pó-lô Sian-siⁿ ta̍k-sî khiā tī káng-toâⁿ to ū koân-ui. Siáⁿ-sū án-ni? I kóng, Goá m̄-káⁿ uî-keh tuì thiⁿ só͘ hián-hiān--ê.</p>
<p>&nbsp; Bô īⁿ-siōng , chiū oh-tit pó-chhî káng-toâⁿ ê koân-ui.</p>
<p>&nbsp; 8. M̄-sī kóng pài-tn̂g toā keng, hoē-iú choē Siōng-tè chiū hoaⁿ-hí. Lâng khoàⁿ-tāng liōng, Siōng-tè khoàⁿ-tāng chit. Chú Iâ-so͘ kóng, Siat-sú lín tiong-kan nn̄g lâng tī toē-nih bô lūn kiû sím-mi̍h, nā-sī tâng-sim, chiū Goá tī thiⁿ-nih ê Pē beh kā in choè-chiâⁿ. In-uī put-lūn sím-mi̍h só͘-chāi ū nn̄g saⁿ lâng tī goá ê miâ chū-hoē, goá iā tī in tiong-kan(Má-thài 18:19,20). Chit nn̄g saⁿ lâng, lóng sī sìn Chú , thiàⁿ Chú, kap Chú liân-ha̍p--ê; só͘-í in ê só͘ choè kap kî-tó lóng ū toā hāu-le̍k. Nā ū Chú Iâ-so͘ tī hit tiong-kan, sui-jiân chió-sò͘ iā ū toā khuì-la̍t. Kàu-hoē ê chóng-le̍k(總力) chāi tī ū it-tì kiat-ha̍p ê sìn-tô͘.</p>
<p><em>&nbsp; 9. Kak-gō oa̍h tī sìn-gióng lâi oa̍h-tāng ê sî-tāi.</em></p>
<p>&nbsp; Chá Mô͘-se kiò Í-sek-lia̍t peh-sìⁿ tio̍h tuì Hô-lia̍t soaⁿ lo̍h-khì(Sin 1:6,7). Tī Hô-lia̍t soaⁿ sī siū chiok-hok , èng-ún un-tián ê só͘-chāi. Kè-khì lán ê kàu-hoē ū siū Siōng-tè ê un-sù choē-choē taⁿ tio̍h lo̍h soaⁿ khì hū-tam Siōng-tè só͘ kau-thok ê chek-jīm. Sè-kài hun-loān ê sî-tāi, sìn-chiá tio̍h kam-goān thiàu-ji̍p che khùn-lân ê sè-kài lâi oa̍h-tāng. <em>Sìn-gióng</em> <em>pò-kok</em> ê ki-hoē m̄-thang sit-lo̍h Tuì che sin Ji̍t-pún ê kòng-hiàn, chiū-sī tio̍h hoat-hui Si̍p-jī-kè ê cheng-sîn; in-uī sin thé-chè ê cheng-sîn-tek ê ki-chhó͘ chiū-sī Si̍p-jī-kè . Si̍p-jī-kè , chiū-sī Ki-tok-kàu ê chin-lí.</p>
<p>&nbsp; <em>10. Si̍t-hiān Ki-tok-kàu ê pún-léng(</em><em>本領</em><em>)</em></p>
<p>&nbsp; Ki-tok-kàu ê pún-léng sī sím-mi̍h? モリソン Phok-sū kóng, Tī le̍k-sú-siōng Siōng-tè ê khé-sī. Oāⁿ oē lâi kóng, Tuì Ki-tok só͘ khé-sī si̍t-chāi-tek ê oa̍h-miā, chiū-sī Ki-tok ê seng-khu. Chiū-sī kàu-thoân; Ha̍p-tông ê Kàu-thoân(合同教團). Ha̍p-tông ê Kàu-thoân , oân-choân hoat-tián, chiah thang kóng sī Ki-tok chin ê seng-khu. iā chiah thang kóng sī chin Iâ-so͘ Kàu-hoē.</p>
<p>&nbsp; Kin-á-ji̍t Ki-tok-kàu liân-bêng só͘ teh chìn-hêng kok phài ha̍p-tông ê sū, sī tú-tú chun-thàn Ki-tok ê kà-sī. Khó-sioh Sèng-kong-hoē í-keng seng-bêng in m̄ chham-ka tī che Kàu-hoē ha̍p-tông lah.</p>
<p>&nbsp; Lâm Pak Kàu-hoē ha̍p-it, che sī Tâi-oân Tiúⁿ-ló Kàu-hoē chi̍t ê khò-tê(課題). Tio̍h kín si̍t-hiān, chiah ū ha̍p Siōng-tè ê chí-ì. Ha̍p-tông Kàu-thoân sêng-li̍p, chiah oē thang kóng sī si̍t-hiān Ki-tok-kàu ê pún-léng.</p>
<p>&nbsp;</p></span>'''

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
    artical10004 = '''<div style="display:none" id="artical_tailo" align="left"><span class="gy12"><p>Sèng-tē hóng-mn̄g-kì(13)</p>
<p>12)Ko-teng (戈登 Gordon) ê Kok-kok-thaⁿ. (1)</p>
<p>(Chiap téng hō tē 11 bīn)</p>
<p>Lâu Hoâ-gī</p>
<p>1962/2/15&nbsp;&nbsp;&nbsp; 16-18</p>
<p>&nbsp;</p>
<p>Ū chi̍t ê siâⁿ lī lán chin hn̄g,</p>
<p>Ū soaⁿ tī hit siâⁿ-goā;</p>
<p>Lán Chú tī hia tèng si̍p-jī-kè,</p>
<p>Siū sí, kiù lí kap goá.</p>
<p>&nbsp;</p>
<p>&nbsp; Lán muí pái gîm chit siú si ê sî, lán ê sim chin siū kám-tōng; in-uī chò si ê sian-seⁿ C.F. Alexander tī chit siú si ê lāi-bīn chin gâu biô-siá Chú siū tèng ê chōng-hóng kap hit ê ì-gī. Koh chok-khek ê sian-seⁿ T.L. Hately gâu phoè khek, tì-kàu hō͘ chit siú si chiâⁿ-chò chhut-miâ ê Sèng-si, hoan-e̍k tī ta̍k-kok ê khiuⁿ-kháu, chiâⁿ-chò tāi-tāi toā-toā sè-sè ê Ki-tok-tô͘ ài gîm ê Sèng-si tiong ê chi̍t siú. Tī chit siú si, chò si ê sian-seⁿ pò lán chai Chú siū tèng ê só͘-chāi Sèng-keng ê kì-sū ū bún-ha̍p. Lūn Iâ-so͘ siū tèng ê só͘-chāi, chiàu Sèng-keng só͘ kì:</p>
<p>1. Tī siâⁿ-goā. Iok-hān 19:17 kóng, "Iâ-so͘ giâ ka-kī ê si̍p-jī-kè <strong>chhut-khì kàu chi̍t ê miâ kiò Thâu-khak-oáⁿ ê só͘-chāi, Hi-pek-lâi ê oē kiò-choè Kok-kok-thaⁿ."Hi-pek-lâi 13:12 kóng, "Iâ-so͘ in-uī beh ēng ka-kī ê hoeh hō͘ peh-sèⁿ chiâⁿ-sèng, ia̍h siū-khó͘ tī siâⁿ-mn̂g goā</strong>."</p>
<p>2.Kūn siâⁿ（lī siâⁿ bô hn̄g）. Iok-hān 19:20 kóng," Iâ-so͘ siū tèng ê só͘-chāi ki<strong>n7 siâⁿ.</strong>"</p>
<p>3.Sī tī lō͘-piⁿ. Má-khó 15:29 kóng,"<strong>Keng-koè ê lâng"</strong> siat-to̍k I ......</p>
<p>4. "Tèng si̍p-jī-kè ê só͘-chāi ū hn̂g"（Iok-hān 19:41）, koh put-chí kīn（19:42）.</p>
<p>5. Hn̂g-lāi ū bōng（Iok-hān 19:41）.</p>
<p>&nbsp; a. Bōng sī tī chio̍h-phia̍h só͘ phah ê (Má-thài 27:60; Lō͘-ka 23:53).</p>
<p>&nbsp; b. bōng sī sin--ê, bē bat ū lâng chòng (Lō͘-ka 23:53).</p>
<p>&nbsp; c.Bōng-kháu ē thang hō͘ chi̍t tè chio̍h lâi that bōng-mn̂g.</p>
<p>&nbsp; d. Chit ê bōng sī chun-kuì ê gī-oân A-lī-má-thài ê Iok-sek su-jîn ê só͘ iú(Má-thài 27:60).</p>
<p>6. Lán ê Chú chiū-sī bâi-chòng tī chit ê bōng. Má-thài 27:60 kóng,"Hē tī i ka-kī ê sin bōng."</p>
<p>&nbsp; Iok 80 nî chêng, ū chi̍t uī Eng-kok ê chiong-kun kiò Ko-teng, i sī jia̍t-sim kèng-khiân ê Ki-tok-tô͘. I tiâu-kang lâi kàu Iâ-lō͘-sat-léng tiau-cha gián-kiù Chú Iâ-so͘ ê sū-chek. I ia̍h sī tuì Sèng-bōng kàu-hoē sit-bāng ê chi̍t ê lâng, só͘-í chiàu téng-bīn só͘ thê-khí Sèng-keng só͘ kì-chài lūn Chú Iâ-so͘ siū tèng ê tiâu-kiāⁿ, chi̍t-hāng chi̍t-hāng lâi chim-chiok, huì liáu chē-chē ê kong-im, sim-sîn kap kim-chîⁿ , chiū tī hiān-chāi Tāi-má-sek siâⁿ-mn̂g kháu ê tang-pak kak iok 250 kong-chhioh ê só͘-chāi ê chi̍t ê soaⁿ-lûn-á kap chiap tī hit ê soaⁿ-lûn-á ê keh-piah ê chi̍t khu hoe-hn̂g, kā i toàn-tēng kóng, chia chiàⁿ sī Chú siū tèng kap bâi-chòng ê só͘-chāi. Chit ê soaⁿ-lûn-á hiān-sî kā i chheng-ho͘ kóng sī Ko-teng ê Kok-kok-thaⁿ, iā hit khu hn̂g in-uī ū chi̍t ê chio̍h-bōng kāi kiò-chò " Têng-oân ê bōng"(庭園的墓).</p>
<p>Tuì Sèng-bōng kàu-hoē chin toā sit-bāng ê goán, suî-sî hō͘ àn-nāi ê lâng chhoā koè Iâ-lō͘-sat-léng ê ke-lō͘ chhut Tāi-má-sek siâⁿ-mn̂g lâi kàu tī "Têng-oân ê bōng." Hiān-sî hn̂g ū ēng koân ê chio̍h-chhiûⁿ uî khí-lâi. Phah-mn̂g ê sî, ū chi̍t uī Kuì-keh-hoē ê koán-lí-oân chhut-lâi kā goán soat-bêng. Hn̂g-lāi iok ū hun goā tē, ū chèng chhiū-ba̍k hoe-chháu, bō͘-sēng koh hó khoàⁿ. I tī chia pò goán khoàⁿ 4 hāng.</p>
<p>I. Ko-teng ê Kok-kok-thaⁿ. I chhoā goán kàu tī hn̂g-lāi ê tang lâm kak ê chi̍t ê koân-tâi. I tuì hia pò goán khoàⁿ tī keh-piah ê chi̍t chō soaⁿ-lûn-á. Chit chō soaⁿ-lûn-á bô chin koân, lī lō͘-bīn iok ū 4 tn̄g koân. Chit chō chio̍h-hoe-chio̍h ê soaⁿ-lûn-á, hiān-sî sī chò Hoê-hoê-kàu-tô͘ ê bōng-po͘. Chit chō soaⁿ-lûn-á ê lâm-pêng ê pō͘-hūn sī toān-gâi(斷崖). Tī hia in-uī ji̍t kú siū hong-song ê hong-hoà(風化) tī chio̍h phiâⁿ ū kuí-nā khang ê tōng-khang. Kî-tiong ū 3 khang pâi 3 kak hêng, nā tuì hn̄g-hn̄g khoàⁿ khí-lâi, tú-tú chhin-chhiūⁿ sí-lâng ê thâu-khak-oáⁿ ê nn̄g luí ba̍k-chiu khang kap phīⁿ-khang ê hêng-chōng. Chiah ê tōng-khang ia̍h kiò-chò Iâ-lī-bí ê tōng-khang. ún-tàng sī kap sian-ti Iâ-lī-bí ê toān-kì ū koan-liân. In-uī uī-tio̍h chit ê soaⁿ-tōng khoàⁿ khí-lâi chhin-chhiūⁿ thâu-khak-oáⁿ, Iû-thài lâng chiah kiò chit só͘-chāi chò Thâu-khak-oáⁿ, koh Ko-teng chiong-kun ia̍h chiah káⁿ toàn-tēng chia chiū-sī chin-chiàⁿ ê Kok-kok-thaⁿ.</p>
<p>II. Chio̍h chha̍k ê bōng. Tī hoe-hn̂g lāi ê pak-pêng chio̍h-phia̍h hia ū chit ê bōng. Chit ê bōng ū chi̍t ê sè-sè ê mn̂g thang chhut-ji̍p, iā tī bōng-kháu ū chit tiâu chio̍h-kau, thang kō toā chio̍h thang sat hit ê mn̂g. Mn̂g ê chiàⁿ-pêng téng-bīn ū chi̍t ê sè-sè khang chò thiⁿ-thang thang chhái-kng. Nǹg ji̍p-khì bōng-lāi, in-uī thiⁿ-thang ê chhái-kng ū kàu-gia̍h, bē kám-kak àm. Lāi-bīn iok 2 tn̄g chhim, tn̄g peh khoah, iā keh chò chha-put-to pêⁿ toā keng ê 2 pō͘-hūn. Tuì mn̂g ji̍p-khì chit pō͘-hūn sī khang-tè, iā kî-thaⁿ hit pō͘-hūn sī pí hit pō͘-hūn khah kē chhioh-goā, tī hia ū 3 ê bōng-khòng, chit 3 ê bōng hêng tú-tú chhin-chhiūⁿ hêng. Lâm-pak pêng-piⁿ lia̍h-pâi kok chi̍t ê, ia̍h tī chit nn̄g ê tiong-kan ū chi̍t ê sè--ê. Bêng-bêng chit ê bōng sī sio̍k tī su-khia ê ka-cho̍k bōng, m̄-sī kong-bōng. Pak-pêng hit ê bōng bat ēng koè liáu, kî-thaⁿ ê 2 ê m̄-bat ēng koè ê jiah. Koán-lí ê lâng chhut-la̍t kiông-tiau kóng chit ê sī Chú ê bōng. In-uī</p>
<p>&nbsp; 1. Sī bē bat ēng koè ê bōng（Iok-hān 19:41）.</p>
<p>&nbsp; 2. Bōng thâu, bōng boé ū sió-khoá ê khang-tē kàu-gia̍h hō͘ 2 ê thiⁿ-sài thang chē tī hia（Má-khó 16:5; Iok-hān 20:12）.</p>
<p>&nbsp; 3. Bōng-lāi ū kàu -gia̍h kng-soàⁿ thang hō͘ Iok-hān tī Chú koh-oa̍h hit chá-hhí<em>(sic.)</em>, tuì bōng-kháu khoàⁿ ji̍p-khì; tī Chú khǹg sin-si ê só͘-chāi ū khǹg hiah ê chat I ê iù-tē-pò͘ chin bêng（Iok-hān 20:4）. Tī thiⁿ tú phú-kng sî ē thang khoàⁿ kàu chiah-nih chheng-chhó, sī in-uī ū thiⁿ-thang ê chhái-kng ê iân-kò͘.</p>
<p>&nbsp; 4. Tī bōng-kháu ū chi̍t tiâu chio̍h-kau thang kō bōng-mn̂g chio̍h.</p>
<p>&nbsp; 5. Bōng-chhiûⁿ ū chi̍t-pō͘-hūn siū kòng-pháiⁿ. Sī in-uī Lô-má hông-tè Trajanus（98-117） ài phah-bia̍t Ki-tok-kàu, só͘-í bēng-lēng huí-hoāi Iâ-so͘ ê sū-chek, chiū chiong I ê bōng kā i kòng-phoàⁿ, koh kā i thūn-ba̍t khí-lâi.</p>
<p>&nbsp; 6. Tī chit ê bōng-kháu ê tē-siōng thang khoàⁿ tio̍h chi̍t ê sé-lé poâⁿ ê chō ê jiah. Só͘-í thang khak-sìn tī chit ê bōng-kháu, kí-hêng si-sián-sek.</p>
<p>&nbsp; III. Hn̂g. Koán-lí ê lâng pí chit-phiàn the̍h-á, kā goán kóng, "Lán</p>
<p>ê Chú m̄-nā bâi-chòng tī chia,koh-oa̍h hit chá-khí ū tī chia chhut-hiān hō͘ Boa̍t-tāi-lia̍p ê Má-lī-a khoàⁿ-kìⁿ." Kì-tit hit chá-khí, &nbsp;Má-lī-a uī-tio̍h chhoē bô Chú ê sin-si teh thî-khàu, Chú chhut-hiān kap i kóng-oē, mn̄g i siáⁿ-sū thî-khàu, teh chhoē sím-mi̍h? I phah-sǹg I sī kò͘ hn̂g ê lâng, kiò I kóng, " Thâu-ke ah......"（Iok-hān 20:11-18）. Ū-iáⁿ, tī chiah ê toā châng bō͘-sēng ê chhiū-ba̍k ê hn̂g-lāi, iông-īⁿ thang siūⁿ chhut hit chá-khí só͘ hoat-seng chit ê sū-si̍t. Tī chit ê hn̂g só͘ ū ê tiâu-kiāⁿ tú-tú kap Hok-im-su ê kì-sū saⁿ-tuì.</p>
<p>&nbsp; I ēng chiah chò lí-iû kui-la̍p ê kiat-lūn sī ài kóng, " chit ê soaⁿ-lûn-á chiàⁿ sī Chú siū tèng ê Kok-kok-thaⁿ, chit hn̂g-á chiàⁿ sī A-lī-má-thài ê Iok-sek ê, chit ê bōng chiàⁿ sī Chú ê bōng. Goán thiaⁿ liáu iā kám-kak put-chí ū lí-khì. In-uī lí-lūn chéng-jiân, chèng-kù chhiong-chiok. In-uī nā m̄-sī Chú ê bōng ū sím-mi̍h lí-iû beh khòng-phoà chit ê khòng-chhiû? Koh ū sím-mi̍h lí-iû kéng tī chit ê bōng-chêng lâi siū sé? Bô-lūn tuì Hok-im-su ê kì-sū, á-sī tuì hiān-hóng ê chhui-sióng lóng thang kap i ê chú-tiuⁿ tông-ì.</p>
<p>(Thāi-sio̍k)</p></span></div>'''
    artical99 = '''  <td valign="top" class="gy12" id="artical_content"><p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">大福氣</span><span lang="EN-US"><br /><span style="font-family: Times New Roman;">1897.04 145 </span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">卷</span><span lang="EN-US"><span style="font-family: Times New Roman;"> p.30<br />1<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">細漢囡仔佮大人</span><span lang="EN-US"><br /></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">蹛世間暫時，向望</span><span lang="EN-US"><br /></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">佇天無閣相離</span><span lang="EN-US"><br /></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">這算大福氣，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">永遠大大福氣，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">這算大福氣，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">咱大家無閣相離。</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br />(</span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">每節紲吟這四句草字。</span><span lang="EN-US"><span style="font-family: Times New Roman;">) </span></span></p>
<p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span lang="EN-US"><span style="font-family: Times New Roman;">2<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">人誠實疼咱救主，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">死了後入父的</span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">厝，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">大家吟詩歡喜。</span></p>
<p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span lang="EN-US"><span style="font-family: Times New Roman;">3<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">細漢囡仔誠實心，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">揣救主求伊憐憫，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">攏總相見無離。</span></p>
<p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span lang="EN-US"><span style="font-family: Times New Roman;">4<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">咱所疼的</span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">序大人，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">兄弟姐妹心相同，</span><span lang="EN-US"><br /></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">聚集無閣相離。</span></p>
<p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span lang="EN-US"><span style="font-family: Times New Roman;">5<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">咱的</span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">心真正歡喜，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">主耶穌佮咱相見，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">坐位榮光無比。</span></p>
<p class="Msoⁿormal" style="margin: 0cm 0cm 0pt;"><span lang="EN-US"><span style="font-family: Times New Roman;">6<br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">咱佇遐稱做聖徒，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">到永遠呵咾耶穌，</span><span lang="EN-US"><span style="font-family: Times New Roman;"><br /></span></span><span style="font-family: 新細明體; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman';">佮伊無閣相離。</span></p></td>'''
    artical11905 = '''<div style="display:none" id="artical_tailo" align="left"><span class="gy12"><p>Sin-nî ê Kng</p>
<p>Siau Lo̍k-siān</p>
<p>Lō͘-ka 11:33-36</p>
<p>194001 658 hō p.23-24</p>
<p><strong>"Bô lâng tiám-teng hē tī ún-ba̍t ê só͘-chāi, á-sī táu-ē, chiū-sī hē tī teng-tâi téng...... Seng-khu ê teng chiū-sī lí ê ba̍k-chiu8......"</strong></p>
<p>Kin-nî sī te̍k-pia̍t ê nî, ǹg-bāng tuì téng-bīn ū te̍k-pia̍t ê kng. Lâng lóng ū keng-kè choē choē sin-nî ê; chóng-sī m̄-chai ū kuí lâng si̍t-chāi chai i sin-nî ê thâu chi̍t-pō͘. Nā m̄-chai i ê thâu-chi̍t pō͘ chiū boē chai i chi̍t nî tiong ê kha-pō͘. M̄-chai i ê thâu-chi̍t pō͘, chiū-sī tuì tī bô bêng-pe̍k i só͘ tio̍h kiâⁿ ê lō͘, tì-kàu bóng kè, bóng kiâⁿ, bóng hoaⁿ-hí, pa̍t lâng hàm-hàm kè, lán iā hàm-hàm kè. Che sī sìn-tô͘ só͘ tio̍h kéng-kái--ê. Iâ-so͘ kóng,"Goá chiū-sī lō͘" Eng-kai lán tio̍h chai lán ê lō͘. Tuì chit chām ê Sèng-keng lán thang lia̍h tio̍h 2 hāng:</p>
<ul>
<li>1. Lán tio̍h gâu ēng sìn-gióng ê kng kap te̍k-koân.</li>
</ul>
<p>&nbsp; Siōng-tè ēng bān-mi̍h hō͘ lán ū chin gâu ēng á bô? Thang chai chin-choē lâng boē hiáu ēng. Siōng-tè só͘ hō͘ lán ê tō-lí sī chhin-chhiūⁿ chiong tiám to̍h ê teng hō͘ lán. Lán kā i hē tī tó-uī? Teng m̄-sī ū teh to̍h chiū hó, sī khoàⁿ ū choè lō͘-ēng á bô. Nā khǹg tī siuⁿ-á- lāi, hit ê teng sī kap bô teng saⁿ-tâng. Teng sī chin hó; chóng-sī tio̍h ū choè lō͘-ēng, ū hōng-sū-sèng chiah sī hó. Lán put-sî thang chiū-kūn Chú; chóng-sī lán m̄-sī kan-ta thiaⁿ tō-lí, bat tō-lí, á-sī kám-ho̍k, á-sī tông-ì nā-tiāⁿ, chiū-sī tio̍h ū choè sì-uî ê lâng ê lō͘-ēng; m̄-sī ū tō-lí iā bô hōng-sū,bô teh choè sì-uî ê lō͘ ēng. "Lâng khoàⁿ-kìⁿ lí ê hó só͘ kiâⁿ....". Tuì Sèng Sîn thang choè chit khoán ê lâng. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>Teng sī chiàu i ê le̍k-liōng teh hoat-chhut kng, ài chhiō khah khoah. Sìn-tô͘ ê sim-koaⁿ tio̍h khoah toā, m̄-thang oe̍h-toe̍h. Chiàu lán sim-lāi só͘ tuì Siōng-tè niá-siū Hok-im ê khuì-la̍t, ài chiò khah hn̄g koh khoah. Ū hó tio̍h saⁿ pò, ài pa̍t lâng kap lán saⁿ-kap tit-tio̍h chiok-hok. Sian-siⁿ ài ha̍k-seng kap i siāng&nbsp; kha-pō͘. Chú-lâng jia̍t-sim sìn Chú, siū tio̍h toā chiok-hok, iā ài chhiàⁿ ê lâng kap i tâng-kiâⁿ. Thoân tō-lí hō͘ pa̍t lâng, chiū-sī tuì chit khoán ê cheng-sîn. Thiàⁿ pa̍t lâng chhin-chhiūⁿ ka-kī, ài hō͘ khah hn̄g, khah khoah ê lâng kap lán saⁿ-kap kiâⁿ tī kng-bêng ê lō͘.</p>
<ul>
<li><em>2. </em><em>Lán ê sim-koaⁿ tio̍h chi̍p-tiong, iā m̄-thang koah choè kuí-nā ê sim.</em></li>
</ul>
<p>"Sin-khu ê teng chiū-sī ba̍k-chiu, lí ê ba̍k-chiu nā kim, thong seng-khu iā kng......"</p>
<p>Lán khiā tī Sin-nî ê thâu-chi̍t ji̍t, tī lán thâu-chêng ū chin-choē tiâu lō͘, ū chin-choē hāng mi̍h, nā boē hiáu kéng hó ê lō͘, hó ê mi̍h sī bô chhái kang. Ba̍k-chiu só͘ khoàⁿ oē tio̍h lóng hó, án-ni i m̄-sī ū hó ê ba̍k-chiu. Choē-choē lâng ài uī-tio̍h chin-lí, iā ài uī-tio̍h jîn-chêng, ài hō͘ Siōng-tè hoaⁿ-hí, iā ài hō͘ lâng hoaⁿ-hí. ài lâi-sè,iā ài kim-sè. ài choè thiⁿ-téng ê lâng lâi seng-oa̍h, iā ài choè chi̍t ê sè-kan lâng. Che sī ba̍k-chiu hoe ê lâng, uī-tio̍h ba̍k-chiu hoe, sim-koaⁿ chiū koah choè kuí-nā ê sim. Ba̍k-chiu hoe sin-khu chiū àm. I ê ba̍k-chiu nā boē hiáu kéng, i ê sin-khu tè i kan-khó͘. I nā gâu kéng tē-it hó ê lō͘ kap tē-it ū kè-ta̍t ê mi̍h, i choân sin chin hok-khì. Khoàⁿ A-pek-lia̍p-hán ê sim, put-lūn Siōng-tè kiò i khì tó-uī i to beh khì, i uī-tio̍h chit hāng lâi seng-oa̍h. Mô͘-so͘ iā sī án-ni. Tāi-pi̍t ông ēng kau-poê Siōng-tè choè tē-it hó, uī-tio̍h án-ni lâi seng-oa̍h. Pó-ló á-sī Lō͘-tek Má-teng in oē choè hiah toā ê kang, chiâⁿ choè hiah uí-tāi ê lâng, bô m̄-sī in uī-tio̍h chit hāng lâi chhut-la̍t, sim-koaⁿ bô hun-soàⁿ. Hiah ê lâng ba̍k-chiu kim in choân seng-gâi ū kng. Lán ta̍k ê sìn-tô͘ tio̍h o̍h in ê seng-oa̍h.</p>
<p>Goān Chú chiong chit 2 hāng siúⁿ-sù goán, hō͘ goán gâu chhut-hoat tī kin-nî ê thâu-chi̍t pō͘, lâi tit-tio̍h Siōng-tè chiok-hok nî-tiong ê ta̍k kha-pō͘.</p></span></div>'''
