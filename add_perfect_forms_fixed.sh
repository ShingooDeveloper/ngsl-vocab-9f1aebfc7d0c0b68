#!/bin/bash

# Remove the last 2 lines (the closing ] and })
head -n -2 prospect_entry.json > temp.json

# Add a comma after the last form
echo "    }," >> temp.json

# Append the three perfect form objects
cat >> temp.json << 'FORMS'
    {
      "type": "present_perfect",
      "label": "現在完了形（has/have + 過去分詞）",
      "text": "has prospected",
      "ipa": "/həz prəˈspɛktɪd/",
      "examples": [
        {
          "en": "We have prospected an entire mountain range here.",
          "ja": "私たちはここで山脈全体を探査してきました。",
          "ipa": "/wi həv prəˈspɛktɪd ən ɪnˈtaɪər ˈmaʊntən ˈreɪndʒ hɪr/",
          "linking": [
            "we have → we は /wi/、have は弱形 /həv/ に弱化。[wi həv] ウィ ハヴ",
            "an entire → an の /n/ が entire の初頭 /ɪ/ に連結。[ən ɪnˈtaɪər] エン インタイアー",
            "range here → range は語末 /dʒ/。here に続く（子音+子音、連結なし）"
          ],
          "kana": "ウィ ハヴ プロースペクティド エン インタイアー マウンテン レンジ ヒアー"
        },
        {
          "en": "She has prospected every angle of this biome.",
          "ja": "彼女はこのバイオームのあらゆる角度を探査してきました。",
          "ipa": "/ʃi həz prəˈspɛktɪd ˈɛvəri ˈæŋɡəl əv ðɪs ˈbaɪoʊm/",
          "linking": [
            "She has → She は /ʃi/、has は弱形 /həz/ に弱化。[ʃi həz] シー ハズ",
            "of this → of は弱形 /əv/。this に続く [əv ðɪs] アヴ ディス",
            "angle of → angle は語末 /l/。of に続く（子音+子音、連結なし）"
          ],
          "kana": "シー ハズ プロースペクティド エヴリー アングル アヴ ディス バイオーム"
        }
      ]
    },
    {
      "type": "past_perfect",
      "label": "過去完了形（had + 過去分詞）",
      "text": "had prospected",
      "ipa": "/həd prəˈspɛktɪd/",
      "examples": [
        {
          "en": "By sunset, we had prospected the whole region.",
          "ja": "日没までに、私たちは全地域を探査していました。",
          "ipa": "/baɪ ˈsʌnˌsɛt | wi həd prəˈspɛktɪd ðə ˈhoʊl ˈridʒən/",
          "linking": [
            "we had → we は /wi/、had は弱形 /həd/ に弱化。[wi həd] ウィ ハド",
            "had prospected → had は弱形 /həd/。prospected に続く（子音+子音、連結なし）",
            "the whole → the は弱形 /ðə/。whole に続く [ðə ˈhoʊl] ザ ホール"
          ],
          "kana": "バイ サンセット、ウィ ハド プロースペクティド ザ ホール リージョン"
        },
        {
          "en": "They realized they had prospected incorrectly and missed valuable ore.",
          "ja": "彼らは不正確に探査していたことに気づき、貴重な鉱石を見逃しました。",
          "ipa": "/ðeɪ ˈriːəˌlaɪzd ðeɪ həd prəˈspɛktɪd ɪnˌkəˈrɛktli ənd ˈmɪst ˈvæljəbəl ˈɔr/",
          "linking": [
            "they had → they は /ðeɪ/、had は弱形 /həd/ に弱化。[ðeɪ həd] ザイ ハド",
            "had prospected → had は弱形 /həd/。prospected に続く（子音+子音、連結なし）",
            "and missed → and は弱形 /ənd/ に弱化。missed に続く [ənd ˈmɪst] アン ミスト"
          ],
          "kana": "ザイ リアライズド ザイ ハド プロースペクティド インコレクトリー アン ミスト ヴァリュアブル オアー"
        }
      ]
    },
    {
      "type": "present_perfect_progressive",
      "label": "現在完了進行形（has/have been + -ing）",
      "text": "has been prospecting",
      "ipa": "/həz bɪn prəˈspɛktɪŋ/",
      "examples": [
        {
          "en": "We have been prospecting this area all morning long.",
          "ja": "私たちは朝ずっとこの地域を探査しています。",
          "ipa": "/wi həv bɪn prəˈspɛktɪŋ ðɪs ˈɛriə ˈɔl ˈmɔrnɪŋ ˈlɔŋ/",
          "linking": [
            "we have → we は /wi/、have は弱形 /həv/ に弱化。[wi həv] ウィ ハヴ",
            "have been → have は弱形 /həv/、been は弱形 /bɪn/。[həv bɪn] ハヴ ビン",
            "been prospecting → been は弱形 /bɪn/。prospecting に続く（子音+子音、連結なし）"
          ],
          "kana": "ウィ ハヴ ビン プロースペクティング ディス エリア オール モーニング ロング"
        },
        {
          "en": "She has been prospecting an exciting deep cave.",
          "ja": "彼女はエキサイティングな深い洞窟を探査し続けています。",
          "ipa": "/ʃi həz bɪn prəˈspɛktɪŋ ən ɪkˈsaɪtɪŋ ˈdip ˈkeɪv/",
          "linking": [
            "She has → She は /ʃi/、has は弱形 /həz/ に弱化。[ʃi həz] シー ハズ",
            "has been → has は弱形 /həz/、been は弱形 /bɪn/。[həz bɪn] ハズ ビン",
            "an exciting → an の /n/ が exciting の初頭 /ɪ/ に連結。[ən ɪkˈsaɪtɪŋ] エン エクサイティング"
          ],
          "kana": "シー ハズ ビン プロースペクティング エン エクサイティング ディープ ケイヴ"
        }
      ]
    }
  ]
}
FORMS

# Replace the original file
mv temp.json prospect_entry.json

echo "Perfect forms added successfully with correct formatting"
