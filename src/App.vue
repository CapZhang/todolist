<template>
  <div id="app">
 <header>ToDoList</header>
  <todo-input/>
  <todo-list/>
  </div>
</template>

<script>
import TodoInput from "./components/input"
import TodoList from "./components/list"
export default {
  name: 'App',
  components:{
    TodoInput,
    TodoList
  }
}
</script>

<style>
ul {
  padding: 0;
  margin: 0;
  list-style: none;
}

p {
  margin: 0;
}
#app {
  width: 400px;
  height: 500px;
  margin: 80px auto;
  padding-top: 20px;
}

header {
  font-size: 28px;
  line-height: 40px;
  text-align: center;
}
.todo-input {
  display: flex;
  margin-bottom: 20px;
}
.todo-input input {
  flex: 1;
  height: 34px;
  margin-right: 20px;
  padding-left: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

.todo-input button {
  width: 70px;
  height: 38px;
  background-color: cadetblue;
  border: none;
  border-radius: 6px;
  color: #fff;
}

.todo-item {
  display: flex;
  height: 40px;
  padding: 0 20px;
}

.todo-item span {
  padding-left: 10px;
}

.todo-item p {
  flex: 1;
}

.todo-item button {
  width: 50px;
  height: 32px;
  background-color: red;
  border: none;
  border-radius: 6px;
  color: #fff;
}

.todo-nodata {
  font-size: 40px;
  line-height: 80px;
  text-align: center;
  color: brown;
}
</style>
