#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Read the current pity_entry.json
with open('pity_entry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the future forms to add
future_forms = [
    {
        "type": "future",
        "label": "単純未来形（will + 動詞原形）",
        "text": "will pity",
        "ipa": "/wɪl ˈpɪti/",
        "examples": [
            {
                "en": "I'll pity any player who loses all their diamonds in lava.",
                "ja": "溶岩でダイヤをすべて失うプレイヤーを哀れに思うでしょう。",
                "ipa": "/aɪl ˈpɪti ˈɛni ˈpleɪɚ hu ˈluzɪz ˈɔl ðɛɹ ˈdaɪmənz ɪn ˈlɑvə/",
                "linking": [
                    "I'll pity → I'll /aɪl/ の縮約形が pity /ˈpɪti/ に続く「アイル ピティ」",
                    "loses all → /z/ が母音 /ɔ/ に連結「ルーズィズ オール」",
                    "their diamonds → their の /ɹ/ が diamond に r-linking「ザイアー ダイモンズ」"
                ],
                "kana": "アイル ピティ エニー プレイアー フー ルーズィズ オール ザイアー ダイモンズ イン ラーヴァ"
            },
            {
                "en": "They'll pity the zombie trapped underwater.",
                "ja": "水中に閉じ込められたゾンビーを彼らは哀れに思うでしょう。",
                "ipa": "/ðɛɹl ˈpɪti ðə ˈzɑmbi ˈtræpt̚ ˌʌndɚˈwɔɾɚ/",
                "linking": [
                    "They'll pity → They'll /ðɛɹl/ の縮約形が pity /ˈpɪti/ に続く「ザイアル ピティ」",
                    "the zombie → the の弱形 /ðə/ が zombie /ˈzɑmbi/ に続く「ザ ゾンビー」",
                    "trapped underwater → trapped の /t/ が未開放「トラプッ」で underwater に続く、water の /t/ がフラップ化「ウォーラー」"
                ],
                "kana": "ザイアル ピティ ザ ゾンビー トラプッ アンダーウォーラー"
            }
        ]
    },
    {
        "type": "future_perfect",
        "label": "未来完了形（will have + 過去分詞）",
        "text": "will have pitied",
        "ipa": "/wɪl həv ˈpɪtid/",
        "examples": [
            {
                "en": "I'll have pitied countless players by the end of this game.",
                "ja": "このゲームの終わりまでに、数え切れないほどのプレイヤーを哀れに思ってくるでしょう。",
                "ipa": "/aɪl həv ˈpɪtɪd ˈkaʊntləs ˈpleɪɚz baɪ ðə ˈɛnd əv ðɪs ˈɡeɪm/",
                "linking": [
                    "I'll have → I'll /aɪl/ と have の弱形 /həv/ が連結「アイル ハヴ」",
                    "countless players → less の語末 /s/ が players の /p/ で「コウントレス プレイアーズ」",
                    "by the → /baɪ/ が定冠詞 the の /ðə/ に続く「バイ ザ」"
                ],
                "kana": "アイル ハヴ ピティッド カウントレス プレイアーズ バイ ザ エンド アヴ ディス ゲイム"
            },
            {
                "en": "They'll have pitied all the lost villagers by tomorrow.",
                "ja": "明日までに、彼らはすべてのはぐれた村人を哀れに思ってくるでしょう。",
                "ipa": "/ðɛɹl həv ˈpɪtɪd ˈɔl ðə ˈlɔst ˈvɪlɪdʒɚz baɪ təˈmɑɹoʊ/",
                "linking": [
                    "They'll have → They'll /ðɛɹl/ と have の弱形 /həv/ が連結「ザイアル ハヴ」",
                    "have pitied → have の弱形 /həv/ が pitied /ˈpɪtɪd/ に続く「ハヴ ピティッド」",
                    "the lost → the の弱形 /ðə/ が lost /ˈlɔst/ に続く「ザ ロースト」"
                ],
                "kana": "ザイアル ハヴ ピティッド オール ザ ロースト ヴィリジャーズ バイ トゥマロー"
            }
        ]
    }
]

# Append the future forms to the existing forms
data['forms'].extend(future_forms)

# Write back to the file
with open('pity_entry.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Added {len(future_forms)} future forms to pity_entry.json")
print(f"Total forms now: {len(data['forms'])}")
print("\nAdded forms:")
for form in future_forms:
    print(f"  - {form['type']}: {form['label']}")
