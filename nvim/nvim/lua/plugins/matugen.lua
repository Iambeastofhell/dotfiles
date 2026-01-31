return {
  {
    "xiyaowong/transparent.nvim",
    lazy = false,
    config = function()
      require("transparent").setup({
        -- This clears the background for these specific groups
        extra_groups = {
          "NormalFloat", -- Floating windows
          "NvimTreeNormal", -- File explorer (if you use it)
          "TelescopeNormal", -- Search windows
          "TelescopeBorder",
          "LazyNormal", -- The Lazy UI
          "MasonNormal", -- The Mason UI
        },
      })
      -- Automatically enable transparency on startup
      vim.cmd("TransparentEnable")
    end,
  },
}
