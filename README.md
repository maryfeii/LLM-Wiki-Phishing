# AI 如何辨識網路釣魚與詐騙訊息？

本專案是一份「來源可追溯的本地 Wiki + HTML 教學簡報」作業原型。網站可直接開啟 `index.html`；不需 API Key。若要公開繳交連結，請部署至 GitHub Pages。

## 內容
- `wiki.html`：六篇官方資料的整理條目，可用關鍵字搜尋。
- `slides.html`：十頁互動教學簡報，支援按鈕、鍵盤左右鍵及小測驗。
- `workflow.html`：Loop / Graph、檢查紀錄與反思。
- `data/sources.json`：六篇官方文件的來源、人工整理摘要及重點。
- `data/wiki_index.json`：十八筆可檢索段落，皆帶來源 ID。
- `docs/SLIDE_SOURCE_MAP.md`：每張投影片對應的來源。
- `docs/CHECK_REPORT.txt`：執行 `python check.py` 的測試結果。
- `build.py`：從結構化 Wiki 來源重新建立網頁；可修改資料再重新執行。

## 資料 ingest 與系統界線
首先以「定義 → 案例 → AI 偵測 → 侷限 → 防護」討論並決定教學範圍。再查閱六篇官方資料，人工擷取各篇摘要、兩個重點及標籤，保存為 `sources.json`。執行 `python build.py` 會將每篇資料切成三個有來源 ID 的片段，輸出 `wiki_index.json`，並生成 Wiki 及簡報網頁。本版本的搜尋是本地關鍵字比對，**不是**真正呼叫外部 LLM / 向量資料庫 / 課堂指定 LLM Wiki 平台的 ingest。六篇來源整理與對應屬於本地 Wiki ingest 原型；如果老師要求特定平台實際操作，需要額外在平台匯入原文或 URL 並保存操作紀錄。

## 測試
```bash
python build.py
python check.py
```
檢查包含：至少五篇、URL、ID 唯一、片段來源可追溯、每頁引用存在、靜態控制項存在。環境的瀏覽器存取受到限制，未能完成自動瀏覽器互動測試；請部署後親自檢查搜尋、翻頁、小測驗與手機排版。

## 免費部署：GitHub Pages
1. 建立 GitHub 公開 Repository，例如 `phishing-llm-wiki`。
2. 將本資料夾**內部所有檔案與子資料夾**上傳至 Repository 根目錄。不要只上傳 ZIP。
3. 進入 **Settings → Pages**，在 **Build and deployment** 設定 **Deploy from a branch**，選擇 `main` 及 `/(root)`，按 **Save**。
4. 等候 GitHub 完成發布後，在 Pages 頁面取得公開網址 `https://<GitHub帳號>.github.io/phishing-llm-wiki/`；以實際顯示的網址為準。
5. Wiki 網址加 `wiki.html`，簡報網址加 `slides.html`。

## 著作與出處
內容是對政府與科技公司資安資料的教學式改寫，並在 Wiki 中保留原始官方網址。案例與簡報結構是為本作業設計。請勿將「AI 分類示範」寫成有執行模型 API 的實驗成果。
