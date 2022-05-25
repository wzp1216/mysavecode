set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=/home/wzp/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'nvie/vim-flake8'
Plugin 'jnurmine/Zenburn'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

colorscheme zenburn
set encoding=utf-8
let python_highlight_all=1
syntax on
set nu
set ts=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent

let g:ycm_global_ycm_extra_conf = 0
