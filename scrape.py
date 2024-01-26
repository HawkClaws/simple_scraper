from urllib.parse import urlparse,urljoin
import requests
from bs4 import BeautifulSoup


def scrape_site_generator(url, target_domain, visited, max_depth, current_depth=0):
    """
    再帰的にウェブサイトをスクレイピングするジェネレータ関数。
    
    :param url: スクレイピングするURL
    :param target_domain: スクレイピング対象のドメイン
    :param visited: 既に訪問したURLのセット
    :param max_depth: リンクをたどる最大の深さ
    :param current_depth: 現在の深さ
    :yield: 各URLのrequests.Responseオブジェクト
    """
    if current_depth > max_depth or url in visited:
        return

    try:
        # URLからドメインを取得
        domain = urlparse(url).netloc

        # 対象ドメインでなければスキップ
        if domain != target_domain:
            return

        # URLにアクセスしてコンテンツを取得
        response = requests.get(url)
        visited.add(url)

        if response.status_code == 200:
            # responseオブジェクトをyield
            yield response

            soup = BeautifulSoup(response.text, 'html.parser')
            # ページ内の全てのリンクを見つけて処理
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                # 相対URLの場合、絶対URLに変換
                absolute_href = urljoin(url, href)
                # 再帰的に同じ関数を呼び出す
                yield from scrape_site_generator(absolute_href, target_domain, visited, max_depth, current_depth + 1)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        