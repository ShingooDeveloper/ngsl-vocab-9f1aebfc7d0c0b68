#!/usr/bin/env python3
import json

# Load the original file
with open('calm_entry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add future forms sections
future_forms = [
    {
        "type": "future",
        "label": "単純未来形",
        "text": "will calm",
        "ipa": "/wɪl ˈkɑːm/",
        "examples": [
            {
                "en": "I will calm the horse with apples before we explore the cave.",
                "ja": "洞窟を探索する前に、リンゴで馬を落ち着かせます。",
                "ipa": "/aɪ wɪl ˈkɑːm ðə ˈhɔrs wɪð ˈæpəlz bɪˈfɔr wi ɪkˈsplɔr ðə ˈkeɪv/",
                "linking": [
                    "before we: before の語末 /r/ が we の /i/ に連結 [bɪˈfɔr wi] → ビフォア ウィー",
                    "the: 子音の前で弱形 /ðə/"
                ],
                "kana": "アイ ウィル カーム ザ ホース ウィズ アップルズ ビフォア ウィー エクスプロア ザ ケイヴ"
            },
            {
                "en": "They will calm the baby villagers by sharing their favorite enchanted apples.",
                "ja": "彼らは好きなエンチャント付きリンゴを共有することで、赤ちゃん村人を落ち着かせるでしょう。",
                "ipa": "/ðeɪ wɪl ˈkɑːm ðə ˈbeɪbi ˈvɪlɪdʒərz baɪ ˈʃɛrɪŋ ðɛr ˈfeɪvərɪt ɪnˈtʃæntɪd ˈæpəlz/",
                "linking": [
                    "their: 子音の前で弱形 /ðɛr/ → ゼア",
                    "enchanted apples: enchanted の語末 /d/ が apples の /æ/ に連結"
                ],
                "kana": "ゼイ ウィル カーム ダ ベイビー ヴィリジャーズ バイ シェアリング ゼア フェイバリット インチャンティド アップルズ"
            }
        ]
    },
    {
        "type": "future_progressive",
        "label": "未来進行形",
        "text": "will be calming",
        "ipa": "/wɪl bi ˈkɑːmɪŋ/",
        "examples": [
            {
                "en": "The jukebox will be calming the aggressive creepers all night long.",
                "ja": "ジュークボックスは一晩中、攻撃的なクリーパーを落ち着かせ続けるでしょう。",
                "ipa": "/ðə ˈdʒuːkˌbɑks wɪl bi ˈkɑːmɪŋ ðə əˈɡrɛsɪv ˈkriːpərz ɔːl ˈnaɪt ˈlɔŋ/",
                "linking": [
                    "creepers all: creepers の語末 /z/ が all の /ɔ/ に連結 [ˈkriːpərz ɔːl] → クリーパーズ オール",
                    "the: 弱形 /ðə/"
                ],
                "kana": "ザ ジュークボックス ウィル ビー カーミング ザ アグレッシヴ クリーパーズ オール ナイト ロング"
            },
            {
                "en": "I'll be calming the wild horses while you finish building the fence.",
                "ja": "あなたが柵を建設し終わるまで、私は野生の馬を落ち着かせ続けます。",
                "ipa": "/aɪl bi ˈkɑːmɪŋ ðə ˈwaɪld ˈhɔrsɪz waɪl ju ˈfɪnɪʃ ˈbɪldɪŋ ðə ˈfɛns/",
                "linking": [
                    "I'll: I will の縮約形 /aɪl/",
                    "the wild: the は子音の前で弱形 /ðə/"
                ],
                "kana": "アイル ビー カーミング ダ ワイルド ホーシーズ ワイル ユー フィニッシュ ビルディング ダ フェンス"
            }
        ]
    },
    {
        "type": "future_perfect",
        "label": "未来完了形",
        "text": "will have calmed",
        "ipa": "/wɪl həv ˈkɑːmd/",
        "examples": [
            {
                "en": "By dawn, I will have calmed all the frightened animals before we start exploring.",
                "ja": "探検を始める前に、夜明けまでに怖がっているすべての動物を落ち着かせます。",
                "ipa": "/baɪ ˈdɔːn | aɪ wɪl həv ˈkɑːmd ɔːl ðə ˈfraɪtənd ˈænɪməlz bɪˈfɔr wi ˈstɑrt ɪkˈsplɔrɪŋ/",
                "linking": [
                    "calmed all: calmed の語末 /d/ が all の /ɔ/ に連結 [ˈkɑːmd ɔːl]",
                    "before we: before の語末 /r/ が we の /i/ に連結 [bɪˈfɔr wi] → ビフォア ウィー",
                    "the: 弱形 /ðə/",
                    "start: 語末 /t/ が exploring の /ɪ/ に続く"
                ],
                "kana": "バイ ドーン、アイ ウィル ハヴ カームド オール ダ フライテンド アニマルズ ビフォア ウィー スター ティクスプローリング"
            },
            {
                "en": "They will have calmed the hostile mobs long before the next raid begins.",
                "ja": "次のレイドが始まるずっと前に、彼らはホスタイルなモブを落ち着かせてしまっているでしょう。",
                "ipa": "/ðeɪ wɪl həv ˈkɑːmd ðə ˈhɑːstaɪl ˈmɑbz ˈlɔŋ bɪˈfɔr ðə ˈnɛkst ˈreɪd bɪˈɡɪnz/",
                "linking": [
                    "have: 弱形 /həv/",
                    "the: 弱形 /ðə/"
                ],
                "kana": "ゼイ ウィル ハヴ カームド ダ ホースタイル モブズ ロング ビフォア ダ ネクスト レイド ビギンズ"
            }
        ]
    }
]

# Add future forms to the forms array
data['forms'].extend(future_forms)

# Save the modified data
with open('calm_entry.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully added future forms to calm_entry.json")
print(f"Total forms now: {len(data['forms'])}")

# Verify the JSON is valid
with open('calm_entry.json', 'r', encoding='utf-8') as f:
    json.load(f)
print("JSON validation successful")
