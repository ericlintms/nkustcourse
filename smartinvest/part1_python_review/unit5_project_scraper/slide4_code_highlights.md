# 投影片 4/4: 程式碼重點解析

## 1. 模擬瀏覽器

```python
headers = {
    'User-Agent': 'Mozilla/5.0 ...'
}
response = requests.get(self.url, headers=headers)
```

## 2. 檢查請求是否成功

```python
# 如果 HTTP 狀態碼不是 2xx (例如 404, 500), 
# 這行會自動引發一個 HTTPError 例外
response.raise_for_status()
```

## 3. 處理所有可能的 `requests` 錯誤

```python
try:
    # ... requests.get ...
    # ... response.raise_for_status ...
except requests.exceptions.RequestException as e:
    # 無論是連線失敗、超時、DNS 錯誤... 都會被捕捉到
    print(f"抓取時發生錯誤: {e}")
```

## 4. 主程式入口 `if __name__ == '__main__':`

* 這段程式碼只有在「直接執行這個 .py 檔案」時才會被執行。
* 如果這個檔案被其他程式 `import`，這段程式碼就不會執行。
* **好處**: 讓你的檔案既可以被當成一個可執行的腳本，也可以被當成一個可供引用的模組。