```
/*
author: Huajin
reference: 
  https://discord.com/channels/686053708261228577/702656734631821413/1155147566615367680
  https://discord.com/channels/686053708261228577/702656734631821413/1073456247849881610
*/

/* @settings

name: SideNote Callout
id: sidenote-callout
settings:
  -
    id: top-sidenote-callout-title
    title: Sidenote Callout Title to Top
    title.zh: 边注标题置于顶部
    type: class-toggle
    default: false
  -
    id: top-left-sidenote-callout-title-position
    title: Top Left Sidenote Callout Title Position
    title.zh: 标注在顶部时，左边注的标题位置
    type: class-select
    default: l-center-callout-title
    options:
      -
        label: left
        value: l-left-callout-title
      -
        label: center
        value: l-center-callout-title
      -
        label: right
        value: l-right-callout-title
  -
    id: top-right-sidenote-callout-title-position
    title: Top Right Sidenote Callout Title Position
    title.zh: 标注在顶部时，右边注的标题位置
    type: class-select
    default: r-center-callout-title
    options:
      -
        label: left
        value: r-left-callout-title
      -
        label: center
        value: r-center-callout-title
      -
        label: right
        value: r-right-callout-title
  -
    id: sidenote-backgound
    title: Callout Background
    title.zh: Callout背景
    description: enable background color
    description.zh: 开启背景色
    type: class-toggle
    default: false
  -
    id: aside-width
    title: sidenote width
    title.zh: 边注宽度
    description: The width of the sidenote
    description.zh: 边注的宽度
    type: variable-number-slider
    default: 200
    min: 150
    max: 300
    step: 10
    format: px
  -
    id: aside-offset
    title: sidenote offset
    title.zh: 边注与正文的间距
    description: The offset between the sidenote and the text(default is 16px)
    description.zh: 边注与正文的间距(默认为16px)
    type: variable-number-slider
    default: 16
    min: 0
    max: 50
    step: 1
    format: px
  -
    id: hide-sidenote-callout-fold-icon
    title: Hide Fold Icon
    title.zh: 隐藏折叠图标
    type: class-toggle
    default: false
*/

body {
  --aside-width: 200px;
  --aside-offset: var(--size-4-4);
  --line-width: var(--file-line-width, --line-width);
}

.markdown-source-view.mod-cm6 .cm-content > .cm-callout:has(.callout[data-callout-metadata*="aside"])[contenteditable=false]  {
  contain: none !important;
  overflow: visible;
}

.markdown-source-view.mod-cm6 .cm-content > .cm-callout:has(.callout[data-callout-metadata*="aside"])[contenteditable=false]>.markdown-rendered {
  overflow: visible;
}

.cm-callout:has(.callout[data-callout-metadata*="aside"])[contenteditable=false]>.edit-block-button {
  display: none;
}

:is(.markdown-source-view .cm-callout, div:not([class])):has(> .callout[data-callout-metadata*="aside"]) {
  position: relative;
  overflow: visible;
}

.callout[data-callout-metadata*="aside"] {
  /* --aside-offset: var(--size-4-4); */
  position: absolute;
}

.callout[data-callout-metadata*="aside-l"] {
  left: calc(-1 * (var(--aside-width) + var(--aside-offset)));
  right: calc(100% + var(--aside-offset));
}

.callout[data-callout-metadata*="aside-r"] {
  left: calc(var(--file-line-width) + var(--aside-offset));
  right: calc(-1 * var(--aside-width));
}

/* .markdown-reading-view .callout[data-callout-metadata*="aside-l"] {
  left: calc(50vw - var(--file-line-width)/2 - var(--aside-width) - 2 * var(--aside-offset));
  right: calc(50vw + var(--file-line-width)/2);
}

.markdown-reading-view .callout[data-callout-metadata*="aside-r"] {
  left: calc(var(--file-line-width) + 2 * var(--aside-width));
  right: calc(50vw - var(--file-line-width)/2 - var(--aside-width) - 2 *var(--aside-offset));
}   */

@media (hover: hover) {
  .markdown-source-view.mod-cm6 .cm-embed-block:has(> div > [data-callout-metadata*="aside"]):hover {
    overflow: visible;
  }
  .markdown-source-view.mod-cm6 .cm-embed-block:not(.cm-table-widget):hover {
    box-shadow: unset;
  }
}

/* ------------ */

.callout[data-callout-metadata*="aside"] {
  --block-spacing: 0.75rem;
  --speaker-block-width: 20%;
  margin: 0px;
  padding: 0px;
  display: grid;
  background-color: var(--background-primary) !important;
  border: none;
}

.sidenote-backgound .callout[data-callout-metadata*="aside"] {
  background-color: rgba(var(--callout-color), 0.1) !important;
  padding-bottom: 10px;
}
.callout[data-callout-metadata*="aside"] {
  grid-template-columns: var(--speaker-block-width) calc(100% - var(--speaker-block-width));
}

.top-sidenote-callout-title .callout[data-callout-metadata*="aside"] {
  grid-template-columns: unset;
}

.callout[data-callout-metadata*="aside"] .callout-title {
  height: calc(100% - var(--block-spacing));
  text-align: right;
  word-wrap: break-word;
  border-right: 3px solid;
  border-bottom: unset;
  flex: 1 0 auto;
  color: rgb(var(--callout-color)) !important;
  background-color: unset !important;
  /* padding-right: var(--block-spacing); */
  padding: 0;
}
.callout[data-callout-metadata*="aside"] .callout-title {
  display: inline-block;
}

body:not(.top-sidenote-callout-title) .setting-item[data-id="top-left-sidenote-callout-title-position"],
body:not(.top-sidenote-callout-title) .setting-item[data-id="top-right-sidenote-callout-title-position"] {
  display: none;
}

.top-sidenote-callout-title .callout[data-callout-metadata*="aside"] .callout-title {
  display: flex;
  flex-direction: row-reverse;
}

.callout[data-callout-metadata*="aside"] .callout-title-inner {
  font-weight: var(--bold-weight) !important;
  color: rgb(var(--callout-color)) !important;
  width: 1ch;
  margin: 0 auto;
  text-align: left;
}

.top-sidenote-callout-title .callout[data-callout-metadata*="aside"] .callout-title-inner {
  margin: 0 auto;
  width: unset;
}

.callout[data-callout-metadata*="aside"] .callout-title-inner {
  margin: 0 auto;
}

.l-left-callout-title .callout[data-callout-metadata*="aside-l"] .callout-title-inner {
  margin-left: var(--block-spacing);
}

.l-right-callout-title .callout[data-callout-metadata*="aside-l"] .callout-title-inner {
  margin: 0 var(--block-spacing);
}

.r-left-callout-title .callout[data-callout-metadata*="aside-r"] .callout-title-inner {
  margin-left: var(--block-spacing);
}

.r-right-callout-title .callout[data-callout-metadata*="aside-r"] .callout-title-inner {
  margin: 0 var(--block-spacing);
}

.callout[data-callout-metadata*="aside"]>* {
  margin-top: var(--block-spacing);
}

.callout[data-callout-metadata*="aside"]>.callout-title>.callout-icon {
  display: none;
}

.hide-sidenote-callout-fold-icon .callout[data-callout-metadata*="aside"] .callout-fold {
  display: none;
}

.callout[data-callout-metadata*="aside"]>.callout-title>.callout-fold,
.callout[data-callout-metadata*="aside"]>.callout-title>.callout-fold.is-collapsed {
  padding: 0;
  justify-content: center;
}

.callout[data-callout-metadata*="aside"]>.callout-content {
  padding: 0px var(--block-spacing);
  border-top: unset;
  max-height: 200px;
  overflow-y: auto;
}

.callout[data-callout-metadata*="aside"]>.callout-content>p:first-child {
  margin-top: 0px;
}

.callout[data-callout-metadata*="aside"]>.callout-content>p:last-child {
  margin-bottom: 0px;
}

.callout[data-callout-metadata*="aside"]>.callout-content::-webkit-scrollbar-thumb {
  width: 11px;
  height: 11px;
  background-color: transparent !important;
}

.callout[data-callout-metadata*="aside"]>.callout-content:hover::-webkit-scrollbar-thumb {
  background-color: var(--scrollbar-thumb-bg) !important;
}

/* ------- */

@media print {
  .callout[data-callout-metadata*="aside-l"] {
    left: 0;
    right: calc(100% - var(--aside-width));
  }
  .callout[data-callout-metadata*="aside-r"] {
    left: calc(100% - var(--aside-width));
    right: 0;
  }
  div:not(.callout-content)>p {
    width: calc(100% - 2 * var(--aside-width));
    margin: 0 auto;
  }
}
```