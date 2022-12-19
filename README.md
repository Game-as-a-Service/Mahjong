# README

## 麻將 - Mahjong 

   * 台灣十六張麻將玩法
   
   
## 使用技術與框架

1. Tech Stack：
   * 後端語言：Python
     * Framework：Fast API
     * DB： MongoDB
   * 前端：Vue 或 React (暫定)
2. Practice Stack：
   * Test-Driven Development
   * Domain-Driven Design
   * Clean Architecture
3. Analysis & Design：
   * Event Storming
   * Example Mapping
   * OOA/D
4. DevOps：
   * Github Action
5. Development：
   * 待定


## Git Commit message

- **Feat:** 新增、修改功能(Feature)。
- **Bug:** 修補 Bug。
- **Docs:** 文件。
- **Refactor:** 重構，既不是新增功能，也不是修補 bug 的程式碼變動。
- **Test:** 增加測試。
- **Chore:** 建構程序或輔助工具的變動 (Maintain)。
- **Revert:** 撤銷回復先前的 Commit 。例如：Revert: scope subject。


## GitHub Flow

1. 團隊任一人皆可依據功能建立issue，並依據需求類型添加 Lebel 及指派人員處理
2. 分支的建立規則：
    *  分支名稱為dev和左斜線與 issue 編號結合
    *  Pattern: `dev/${issueId}`，範例： dev/1 
3. 本地開發測試完成之後，並push本地分支到遠端
4. 發出Pull Request，於 commit 裡填寫 issue link，請求 Reviewer Review Code
5. 需有 2 人 Review PR
    * Mahjong Team members could review the PR.
6. 待 Reviewer 均確認無誤後，通知開發人員已確認完成
7. 開發人員將此 PR 合進 Master 並 closed issue
