import Vue from 'vue';
import VueRouter from 'vue-router';
import StoryPage from '@/views/StoryPage.vue';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'main',
		component: () => import('@/views/MainPage.vue'),
	},
	{
		path: '/guide',
		name: 'guide',
		component: () => import('@/views/GuidePage.vue'),
	},
	{
		path: '/login',
		name: 'login',
		component: () => import('@/views/LoginPage.vue'),
	},
	{
		path: '/signup',
		name: 'signup',
		component: () => import('@/views/SignupPage.vue'),
	},
	{
		path: '/story/:myStoryId/:subStoryId',
		name: 'story',
		props: route => ({
			myStoryId: Number(route.params.myStoryId),
			subStoryId: Number(route.params.subStoryId),
		}),
		// component: () => import('@/views/StoryPage.vue'),
		component: StoryPage,
	},
	{
		path: '/bookshelf',
		name: 'bookshelf',
		component: () => import('@/views/BookshelfPage.vue'),
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import('@/views/profile/ProfilePage.vue'),
	},
	{
		path: '/profile/modifyinfo',
		name: 'modifyinfo',
		component: () => import('@/views/profile/ModifyInfoPage.vue'),
	},
	{
		path: '*',
		redirect: '/404',
	},
	{
		path: '/404',
		component: () => import('@/views/NotFoundPage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
