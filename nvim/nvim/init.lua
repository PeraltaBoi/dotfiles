require("config.remap")
require('config')
require('config.packer')
require("mason").setup({
    ui = {
        icons = {
            package_installed = "✓",
            package_pending = "➜",
            package_uninstalled = "✗"
        }
    }
})
--require('copilot').setup()
require('lspconfig')
vim.o.background = "dark" -- or "light" for light mode
--vim.cmd([[colorscheme gruvbox]])
vim.cmd([[colorscheme catppuccin]])
vim.cmd([[set completeopt=menuone,noinsert,noselect]])
