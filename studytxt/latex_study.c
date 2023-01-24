
########格式控制###################
\par 换行
\newpage  换页











////////////////////////////////////////////////////////////////////
install:
sudo apt install texlive-latex-base  latex-cjk-all texlive-latex-extra texlive-xetex texlive-publisher;

edit .vimrc:
Plugin 'lervag/vimtex'
and run :PluginInstall;
//////////////////////////////////////////////////////////////////
//常用命令
\ll   编译lex文件；
\lv   预览PDF文件；

//test ctex:
\documentclass[fontset=windows]{article}  //install windows font;
\usepackage{ctex}
\begin{document}
你好，\latex!
\end{document}

run:xelatex ctextest.tex

//////////////////////////////////////////////////////////////////
//setting
TEXMFHOME  用于存放用户的包；一般为~/texmf/tex/latex/
一般STY文件放在 /usr/local/texlive/texmf-local 目录下；
加入STY文件后，运行 mktexlsr进行更新；
find my latex dir:
kpsewhich -var-value=TEXMFHOME;
kpsewhich -var-value=TEXMFLOCAL;

缺少sty文件，可以到 ctan.org 进行下载；
texhash 可以更新宏包数据库；

/////////////////////////////////////////////////////////////
//.vimrc setting:
let g:tex_flavor='latex'
TEX文件自动识别语法风格；
let g:tex_conceal='abdmg'
set conceallevel=1
上两行可以让符号直接显示；

let g:vimtex_compiler_latexmk = {
            \ 'build_dir' : {-> 'out'},
            \ 'executable' : 'latexmk',
            \ 'options' : [
            \   '-xelatex',
            \   '-file-line-error',
            \   '-synctex=1',
            \   '-interaction=nonstopmode',
            \ ],
            \}
设置编译工具，输出到OUT目录；
为了更好显示中文；~/.latemkrc 中加上 $pdf_mode=5;

let g:vimtex_compiler_latexmk_engines={'_':'-xelatex'}
let g:vimtex_compiler_latexrun_engines={'_':'-xelatex'}
let g:vimtex_view_method = 'zathura'

edit ~/.config/zathura/zathurarc
set synctex true

vim 编辑 TEX文件，换行必须加一空行；

