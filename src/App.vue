<template>
  <div id="app">
    <div class="sidebar">
      <button>首页</button>
      <button>待办事项</button>
    </div>
    <div class="todo">
      <div class="topbar"></div>
      <div class="content">
        <div class="todo-todo">
        <todo-read />
        <header>ToDoList</header>
        <todo-input />
        <todo-list />
        <todo-save />
      </div>
      <div class="resize" v-on:mousedown="dragResize"></div>
      <div class="todo-details">这里填写备注</div>
      </div>
    </div>
  </div>
</template>

<script>
import TodoInput from "./components/input";
import TodoList from "./components/list";
import TodoRead from "./components/readJson";
import TodoSave from "./components/saveTodo";
import "./themes/defaut-dark/defaut-dark.css";


export default {
  name: "App",
  components: {
    TodoInput,
    TodoList,
    TodoRead,
    TodoSave,
  },
  methods: {
    dragResize(e) {
      // 拖动中间竖线改变待办列表和备注区域的布局宽度
      let resize = document.getElementsByClassName("resize")[0];
      let left = document.getElementsByClassName("todo-todo")[0];
      let right = document.getElementsByClassName("todo-details")[0];
      let box = document.getElementsByClassName("todo")[0];
      let startX = e.clientX;
      resize.left = resize.offsetLeft;
      document.onmousemove = function (e) {
        let endX = e.clientX;
        let moveLen = resize.left + (endX - startX);
        let maxT = box.clientWidth - resize.offsetWidth;
        if (moveLen < 250) moveLen = 250;
        if (moveLen > maxT - 250) moveLen = maxT - 250;
        resize.style.left = moveLen;
        left.style.width = moveLen + "px";
        right.style.width = box.clientWidth - moveLen - 28 + "px";
      };
      document.onmouseup = function (evt) {
        console.log(evt);
        document.onmousemove = null;
        document.onmouseup = null;
        resize.releaseCapture && resize.releaseCapture();
      };
      resize.setCapture && resize.setCapture();
      return false;
    },
  },
};
</script>
