import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 定义变量
    list: ["吃饭s", "睡觉s", "撸猫s"],
    items: []
  },
  mutations: {
    // 定义逻辑
    ADD_ITEM(state, text) {
      state.items.push.apply(state.items,text)
    },
    REMOVE_ITEM(state, index) {
      state.items.splice(index);
    },
    READ_ITEMS(state, jsonitems) {
      // 这里不能使用concat是因为concat不改变原数组
      state.items.push.apply(state.items,jsonitems)
    }
  },
  actions: {
    // 提交（执行）逻辑
    addItem({ commit }, text) {
      commit("ADD_ITEM", text);
    },
    removeItem({ commit }, index) {
      commit("REMOVE_ITEM", index);
    },
    readItems({ commit }, jsonitems){
      commit("READ_ITEMS", jsonitems);
    }
  },
  modules: {},
});
