module.exports = {
	css: {
		loaderOptions: {
			sass: {
				prependData: `
                @import "~@/assets/scss/_variables.scss";
                @import "~@/assets/scss/_mixins.scss";
                @import "~@/assets/scss/_books.scss";
				@import "~@/assets/scss/test/_hong.scss";
				@import "~@/assets/scss/test/_hwang.scss";
				@import "~@/assets/scss/test/_kim.scss";
                `,
			},
		},
	},
};
