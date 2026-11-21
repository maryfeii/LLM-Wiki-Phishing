from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
r=Path(__file__).parent
src=json.loads((r/'data/sources.json').read_text()); chunks=json.loads((r/'data/wiki_index.json').read_text()); slides=json.loads((r/'data/slides.json').read_text()); ids={s['id'] for s in src};tests=[]
def test(name,ok,detail):tests.append((name,bool(ok),detail))
test('至少五篇來源',len(src)>=5,f'{len(src)} 篇')
test('來源 ID 不重複',len(ids)==len(src),f'{len(ids)} 個 ID')
test('來源 URL 完整',all(s['url'].startswith('https://') for s in src),'全部 HTTPS')
test('資料片段可追溯',all(c['source_id'] in ids for c in chunks),f'{len(chunks)} 個片段')
test('每篇三個檢索片段',all(sum(c['source_id']==s['id'] for c in chunks)==3 for s in src),'每篇摘要 1 + 重點 2')
test('簡報共十頁',len(slides)==10,f'{len(slides)} 頁')
test('每頁有引用且可對應 Wiki',all(set(s[4])<=ids and bool(s[4]) for s in slides),'10/10 頁')
for f in ['index.html','wiki.html','slides.html','workflow.html','assets/style.css']:
 test('檔案存在：'+f,(r/f).exists(),f)
test('簡報切換控制',all(x in (r/'slides.html').read_text() for x in ['id="next"','id="prev"','ArrowRight','ArrowLeft']),'按鈕+鍵盤')
test('Wiki 搜尋控制',all(x in (r/'wiki.html').read_text() for x in ['id="q"','addEventListener','data-search']),'搜尋框+監聽')
test('互動小測驗',all(x in (r/'slides.html').read_text() for x in ['data-answer="correct"','id="feedback"']),'回饋+正確答案')
passed=sum(ok for _,ok,_ in tests)
report='LLM Wiki 專案檢查紀錄\n執行方式：python check.py\n檢查類型：本機靜態結構與來源引用完整性\n\n'+'\n'.join(f"{'PASS' if ok else 'FAIL'} | {name} | {detail}" for name,ok,detail in tests)+f'\n\n總結：{passed}/{len(tests)} 通過\n'
(r/'docs/CHECK_REPORT.txt').write_text(report,encoding='utf-8')
print(report)
sys.exit(0 if passed==len(tests) else 1)
