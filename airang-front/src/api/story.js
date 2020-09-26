import { stories } from './index';

export function fetchStories() {
	return stories.get('');
}
export function fetchStory(storyId) {
	return stories.get(`/${storyId}/`);
}
export function fetchMyStories() {
	return stories.get('/mystories/');
}
export function deleteMyStories(storyId) {
	return stories.delete(`/mystories/${storyId}/`);
}
export function fetchSubStories(storyId) {
	return stories.get(`/${storyId}/substories/`);
}
export function fetchBranch(branchId) {
	return stories.get(`/branches/${branchId}/`);
}
export function createMyStory({ story_id, story_name }) {
	return stories.post('/mystories/', { story_id, story_name });
}
export function fetchSubStory({ mystory_id, substory_id }) {
	return stories.get(`/mystories/${mystory_id}/substories/${substory_id}/`);
}
export function finishedMyStory(myStoryId, storyList) {
	return stories.post(`/mystories/${myStoryId}/`, { substory_list: storyList });
}
