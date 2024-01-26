# 再帰的ウェブスクレイピングスクリプト

このスクリプトは、指定されたドメイン内のウェブサイトを再帰的にスクレイピングします。特定のURLから開始し、そのページにある全てのリンクをたどり、リンク先のページも同様にスクレイピングします。

## 使用方法

1. `start_url` にスクレイピングを開始するURLを設定します。
2. `target_domain` にスクレイピング対象のドメインを設定します。
3. `max_depth` にリンクをたどる最大の深さを設定します。
4. スクリプトを実行すると、指定されたドメイン内のページから `requests.Response` オブジェクトが順に返されます。

## コード例

```python
start_url = "https://example.com"  # スクレイピングを開始するURL
target_domain = "example.com"  # スクレイピング対象のドメイン
for response in scrape_site_generator(start_url, target_domain, set(), 2):
    # ここで各responseを処理する
    print(f"Got response from {response.url}")

```

## 要件
- Python 3
- BeautifulSoup4
- requests

## 注意事項
- スクレイピングする際は、対象ウェブサイトの利用規約を遵守してください。
- サーバーに過度な負荷をかけないように注意し、適切な速度制限を設定してください。
- robots.txt を確認し、ウェブサイトのスクレイピングポリシーに従ってください。  

## 余談
余談以外全部GPT4で作りました😛