class Lable {
  constructor(text) {
  this.element = document.createElement("label");
  this.element.innerText = text;
  }
  }
  class Button {
  constructor(text, color = null) {
  this.element = document.createElement("button");
  this.element.innerText = text;
  if (color !== null) {
  this.element.style.color = color;
  }
  }
  }
  class Input {
  constructor(parent, { name, type, placeholder, value, label, max, min }) {
  this.element = document.createElement("input");
  this.element.name = name;
  this.element.type = type;
  this.element.placeholder = placeholder;
  this.element.value = value;
  this.element.id = name;
  if (label !== undefined) {
  label = new Lable(label.text);
  label.element.for = this.element.id;
  parent.appendChild(label.element);
  }
  if (this.element.name == "completed") {
  this.element.addEventListener("click", (e) => {
  let check = this.element.checked;
  this.element.value = check;
  });
  }
  if (max !== undefined && min !== undefined) {
  this.element.addEventListener("change", (e) => {
  if (
  this.element.value.length > max ||
  this.element.value.length < min
  ) {
  this.element.style.color = "red";
  this.element.value = `${name} bigger then ${max} or smaller then ${min}`;
  } else {
  this.element.style.color = "";
  }
  });
  this.element.addEventListener("focus", (e) => {
  if ((this.element.style.color = "red")) {
  this.element.style.color = "";
  this.element.value = "";
  }
  });
  }
  parent.appendChild(this.element);
  }
  }
  const settingTodos = [
  {
  name: "userId",
  type: "number",
  placeholder: "enter userId for Todos",
  value: "",
  label: {
  text: "userId"
  }
  },
  {
  name: "title",
  type: "text",
  placeholder: "enter title for Todos",
  value: "",
  max: 50,
  min: 10,
  label: {
  text: "Title"
  }
  },
  {
  name: "completed",
  type: "checkbox",
  placeholder: "enter completed for Todos",
  value: "",
  label: {
  text: "completed"
  }
  }
  ];
  class MyTodo {
  constructor(parent, todoData) {
  this.div = document.createElement("div");
  this.h1 = document.createElement("h1");
  this.h2 = document.createElement("h2");
  this.p = document.createElement("h3");
  this.hr = document.createElement("hr");
  this.btn = new Button("delete_todo", "purple");
  this.btnUpdateMod = new Button("update_todo", "blue");
  this.btnSaveMod = new Button("save_todo", "orange");
  this.h1.innerText = todoData.title;
  if(todoData.completed == true){
    this.h2.innerText = "Completed"
    this.p.innerText = "Thanks"}
    else{this.h2.innerText = "In process"
    this.p.innerText = "You must do this"}
  this.p.style.color = "black"
  this.p.style.background = "red";
  this.inputh1 = new Input(parent, {
  value: this.h1.innerText,
  type: "text"
  });
  this.inputh2 = new Input(parent, {
  name: "completed",
  value: this.h2.checked,
  type: "checkbox"
  });
  this.btnSaveMod.element.style.display = "none";
  this.inputh1.element.style.display = "none";
  this.inputh2.element.style.display = "none";
  this.div.appendChild(this.h1);
  this.div.appendChild(this.h2);
  this.div.appendChild(this.p);
  this.div.appendChild(this.inputh1.element);
  this.div.appendChild(this.inputh2.element);
  this.div.appendChild(this.btn.element);
  this.div.appendChild(this.btnUpdateMod.element);
  this.div.appendChild(this.btnSaveMod.element);
  this.div.appendChild(this.hr);
  if (parent.firstChild) {
  parent.insertBefore(this.div, parent.firstChild);
  } else {
  parent.appendChild(this.div);
  }
  this.btn.element.addEventListener("click", (e) => {
  $.ajax({
  url: `https://jsonplaceholder.typicode.com/todos/${todoData.id}`,
  method: 'DELETE',
  success: () => parent.removeChild(this.div)
  })
  })
  this.btnUpdateMod.element.addEventListener("click", (e) => {
  this.btnSaveMod.element.style.display = "";
  this.inputh1.element.style.display = "";
  this.inputh2.element.style.display = "";
  this.btnUpdateMod.element.style.display = "none";
  this.h1.style.display = "none";
  this.h2.style.display = "none";
  this.btn.element.style.display = "none";
  });
  this.btnSaveMod.element.addEventListener("click", (e) => {
  $.ajax({
  url: `https://jsonplaceholder.typicode.com/todos/${todoData.id}`,
  method: 'PATCH',
  data: {
  title: this.inputh1.element.value,
  completed: this.inputh2.element.value
  },
  success: todoData => {
  this.h1.innerText = todoData.title;
  this.h2.innerText = todoData.completed;
  this.inputh1.element.value = todoData.title;
  this.inputh2.element.value = todoData.completed;
  }
  });
  this.btnSaveMod.element.style.display = "none";
  this.inputh1.element.style.display = "none";
  this.inputh2.element.style.display = "none";
  this.btnUpdateMod.element.style.display = "";
  this.h1.style.display = "";
  this.h2.style.display = "";
this.btn.element.style.display = "";
});
}
}
class Page {
constructor(setting) {
this.inputDiv = document.createElement("div");
document.body.appendChild(this.inputDiv); 
this.outputDiv = document.createElement("div");
document.body.appendChild(this.outputDiv);

$.ajax({
url: 'https://jsonplaceholder.typicode.com/todos',
method: 'GET',
contentType: 'json',
data: 'application/json',
success: (data) =>
data.map((item) => new MyTodo(this.outputDiv, item))
});
this.button = new Button("Send request");
this.pageInputs = setting.map((item) => new Input(this.inputDiv, item));
this.button.element.addEventListener("click", (e) => {
if (this.pageInputs.find((item) => item.element.style.color === "red")) {
return;
}
let data = this.pageInputs.reduce((acc, item) => {
acc[item.element.name] = item.element.value;
return acc;
}, {});
this.pageInputs.forEach((input) => {
input.element.value = "";
});
$.ajax({
url: 'https://jsonplaceholder.typicode.com/todos',
method: 'POST',
data: data,
success: item => new MyTodo(this.outputDiv, item),
});
})
this.inputDiv.appendChild(this.button.element);
}}
window.addEventListener("load", function(event) {
console.log("All success!");
new Page(settingTodos)
})