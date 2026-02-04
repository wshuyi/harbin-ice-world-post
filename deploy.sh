#!/bin/bash

REPO_NAME="harbin-ice-world-post"
DESCRIPTION="哈尔滨冰雪大世界 - Instagram风格分享页面"

echo "🚀 开始部署到 GitHub..."

# 检查是否已有远程仓库
if git remote get-url origin 2>/dev/null; then
    echo "📦 已有Git仓库，推送中..."
    git add -A
    git commit -m "Update Instagram post page" 2>/dev/null || echo "没有新改动"
    git push origin main
else
    echo "🆕 创建新GitHub仓库..."
    
    # 创建仓库（不初始化本地）
    gh repo create $REPO_NAME --public --description "$DESCRIPTION" --template=null
    
    # 初始化Git
    git init
    git add -A
    git commit -m "Initial commit: Instagram style Harbin Ice World post"
    
    # 添加远程仓库
    git remote add origin https://github.com/wshuyi/$REPO_NAME.git
    
    # 推送到GitHub
    git push -u origin main
    
    echo ""
    echo "✅ 仓库创建成功！"
fi

# 启用GitHub Pages
echo ""
echo "🔧 正在启用 GitHub Pages..."
gh api repos/wshuyi/$REPO_NAME/pages \
  -X PUT \
  -f source='{"branch":"main","path":"/"}' \
  -H "Accept: application/vnd.github+json" 2>/dev/null || \
gh api repos/wshuyi/$REPO_NAME/pages \
  -X POST \
  -f source='{"branch":"main","path":"/"}' \
  -H "Accept: application/vnd.github+json" 2>/dev/null || \
echo "⚠️  Pages 可能已启用或需要手动配置"

echo ""
echo "🎉 部署完成！"
echo "📱 访问地址: https://wshuyi.github.io/$REPO_NAME/"
echo ""
echo "⏳ Pages 首次部署可能需要1-2分钟生效"
echo "📖 查看仓库: https://github.com/wshuyi/$REPO_NAME"
