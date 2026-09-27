#!/usr/bin/env python3
import json

# Read the existing JSON file
with open('stem_entry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the three perfect forms
perfect_forms = [
    {
        "type": "present_perfect",
        "label": "現在完了形（has/have + 過去分詞）",
        "text": "has stemmed",
        "ipa": "/həz ˈstɛmd/",
        "examples": [
            {
                "en": "I have stemmed the water flow by placing sand blocks.",
                "ja": "砂のブロックを配置することで、水の流れを遮りました。",
                "ipa": "[aɪ həv ˈstɛmdə ˈwɔtər floʊ baɪ ˈpleɪsɪŋ sænd blɑks]",
                "linking": [
                    "have は助動詞で弱形 /həv/",
                    "stemmed の末尾子音 /d/ が the の初頭母音 /ə/ に連結。the は冠詞で弱形 /ðə/ [ˈstɛmdə] ステムダ",
                    "by は /baɪ/、placing に続く（子音+子音、連結なし）"
                ],
                "kana": "アイ ハヴ ステムダ ウォーター フロー バイ プレイシング サンド ブロックス"
            },
            {
                "en": "The defensive wall has stemmed the creeper outbreak.",
                "ja": "防御壁がクリーパーの大発生を阻止しました。",
                "ipa": "[ðə dɪˈfɛnsɪv wɔləz ˈstɛmdə ˈkriːpər ˈaʊtbreɪk]",
                "linking": [
                    "the は冠詞で弱形 /ðə/",
                    "wall の末尾子音 /l/ が has の初頭母音 /ə/ に連結。has は助動詞で弱形 /əz/ に弱化 [wɔləz] ウォーレズ",
                    "stemmed の末尾子音 /d/ が the の初頭母音 /ə/ に連結。the は冠詞で弱形 /ðə/ [ˈstɛmdə] ステムダ"
                ],
                "kana": "ザ ディフェンシヴ ウォーレズ ステムダ クリーパー アウトブレイク"
            }
        ]
    },
    {
        "type": "past_perfect",
        "label": "過去完了形（had + 過去分詞）",
        "text": "had stemmed",
        "ipa": "/hæd ˈstɛmd/",
        "examples": [
            {
                "en": "We had stemmed the lava by the time help arrived.",
                "ja": "助けが到着したときには、私たちは既に溶岩を遮っていました。",
                "ipa": "[wi həd ˈstɛmdə ˈlɑvə baɪ ðə taɪm hɛlp əˈraɪvd]",
                "linking": [
                    "had は弱形 /həd/ に弱化",
                    "stemmed の末尾子音 /d/ が the の初頭母音 /ə/ に連結。the は冠詞で弱形 /ðə/ [ˈstɛmdə] ステムダ",
                    "time の末尾子音 /m/ が help の初頭子音 /h/ に続く（子音+子音、連結なし）"
                ],
                "kana": "ウィ ハド ステムダ ラーヴァ バイ ザ タイム ヘルプ ア ライヴド"
            },
            {
                "en": "The barrier had stemmed the invasion before reinforcements arrived.",
                "ja": "援軍が到着する前に、防壁は既に侵攻を阻止していました。",
                "ipa": "[ðə ˈbæriər həd ˈstɛmdə ɪnˈveɪʒən bɪˈfɔr ˌrinˈfɔrsməns əˈraɪvd]",
                "linking": [
                    "had は弱形 /həd/ に弱化",
                    "stemmed の末尾子音 /d/ が the の初頭母音 /ə/ に連結。the は冠詞で弱形 /ðə/ [ˈstɛmdə] ステムダ",
                    "invasion の末尾子音 /n/ が before の初頭子音 /b/ に続く（子音+子音、連結なし）"
                ],
                "kana": "ザ バリアー ハド ステムダ インヴェイジョン ビフォー レインフォースメンツ ア ライヴド"
            }
        ]
    },
    {
        "type": "present_perfect_progressive",
        "label": "現在完了進行形（has/have been + 現在分詞）",
        "text": "has been stemming",
        "ipa": "/həz bɪn ˈstɛmɪŋ/",
        "examples": [
            {
                "en": "We have been stemming the water flow for a long time.",
                "ja": "私たちはずっと水の流れを止めています。",
                "ipa": "[wi həv bɪn ˈstɛmɪŋ ðə ˈwɔtər floʊ fɚə lɔŋ taɪm]",
                "linking": [
                    "have は助動詞で弱形 /həv/",
                    "been は弱形 /bɪn/。n が stemming の /s/ に続く（子音+子音、連結なし）",
                    "the は冠詞で弱形 /ðə/",
                    "for の末尾子音 /r/ が a の初頭母音 /ə/ に連結 [fɚə] ファー"
                ],
                "kana": "ウィ ハヴ ビン ステミング ザ ウォーター フロー ファー ロング タイム"
            },
            {
                "en": "She has been stemming the creeper invasion all week.",
                "ja": "彼女は1週間ずっとクリーパーの侵攻を止め続けています。",
                "ipa": "[ʃi həz bɪn ˈstɛmɪŋ ðə ˈkriːpɚɪn ˈveɪʒən ɔl wik]",
                "linking": [
                    "has は助動詞で弱形 /həz/",
                    "been は弱形 /bɪn/。n が stemming の /s/ に続く（子音+子音、連結なし）",
                    "the は冠詞で弱形 /ðə/",
                    "creeper の末尾子音 /r/ が invasion の初頭母音 /ɪ/ に連結 [ˈkriːpɚɪn] クリーパーイン"
                ],
                "kana": "シー ハズ ビン ステミング ザ クリーパーイン ヴェイジョン オール ウィーク"
            }
        ]
    }
]

# Add the perfect forms to the forms array
data['forms'].extend(perfect_forms)

# Write the updated JSON back to the file
with open('stem_entry.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(perfect_forms)} perfect form entries")
print(f"Total forms in entry: {len(data['forms'])}")
