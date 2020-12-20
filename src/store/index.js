import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 定义变量
    items: []
  },
  mutations: {
    // 定义逻辑
    ADD_ITEM(state, text) {
      state.items.push.apply(state.items,text)
    },
    REMOVE_ITEM(state, index) {
      for(let i=0;i<state.items.length;i++){
        if(i == index){
          state.items.splice(index,1);
          break;
        }
      }
    },
    READ_ITEMS(state, jsonitems) {
      // 这里不能使用concat是因为concat不改变原数组
      console.log("read_items");
      state.items=jsonitems
    },
    UPDATE_ITEMS(state,update_status){
      state.items[update_status.index].type = "update";
      state.items[update_status.index].status = update_status.status;
      if(update_status.status=="doing"){
        let start_list = state.items[update_status.index].start_time
        if (start_list){
          state.items[update_status.index].start_time.push(update_status.time)
        }else{
          state.items[update_status.index].start_time = new Array(update_status.time)
        }
      }else if(update_status.status=="stop"){
        let stop_list = state.items[update_status.index].end_time
        if (stop_list){
          state.items[update_status.index].end_time.push(update_status.time)
        }else{
          state.items[update_status.index].end_time = new Array(update_status.time)
        }
      }
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
    },
    updateItems({commit},update_status){
      commit("UPDATE_ITEMS",update_status);
    }
  },
  modules: {},
});
