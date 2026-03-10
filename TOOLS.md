# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

---

## Lessons Learned

### 2026-03-02: 部署网页不要暴露 VPS IP

**教训**：贪吃蛇游戏首次部署时，直接用 VPS IP + Python HTTP 服务器提供访问，暴露了用户 VPS 的 IP 地址。

**正确做法**：使用 Cloudflare Pages 或 GitHub Pages 部署静态网页，不要用本地 IP。

**操作**：
- ✅ 使用 `cloudflare-pages-deployer` skill 部署到 `yushuzhilan.pages.dev`
- ❌ 禁止使用 `python -m http.server` + VPS IP 的方式

---

