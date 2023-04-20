require("mason").setup()
require("mason-lspconfig").setup({
    ensure_installed = {
        "lua_ls",
        "clangd",
        "eslint",
        "jdtls",
        "pylsp",
        "rust_analyzer",
        "tsserver",
        "vtsls",
    }
})

require("lspconfig").lua_ls.setup {}
require("lspconfig").eslint.setup {}
require("lspconfig").clangd.setup {}
require("lspconfig").jdtls.setup {}
require("lspconfig").pylsp.setup {}
require("lspconfig").rust_analyzer.setup {}
require("lspconfig").tsserver.setup {}
require("lspconfig").vtsls.setup {}
