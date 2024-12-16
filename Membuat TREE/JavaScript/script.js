class TreeNode {
  constructor(value) {
    this.value = value;
    this.children = [];
  }

  addChild(childNode) {
    this.children.push(childNode);
  }

  removeChild(childValue) {
    this.children = this.children.filter((child) => child.value !== childValue);
  }

  display(level = 0) {
    let result = " ".repeat(level * 4) + `- ${this.value}\n`;
    for (const child of this.children) {
      result += child.display(level + 1);
    }
    return result;
  }
}

class InteractiveTree {
  constructor() {
    this.root = null;
  }

  setRoot(value) {
    if (this.root === null) {
      this.root = new TreeNode(value);
    } else {
      alert("Root already exists. Use the existing root.");
    }
  }

  findNode(currentNode, value) {
    if (!currentNode) return null;
    if (currentNode.value === value) return currentNode;

    for (const child of currentNode.children) {
      const found = this.findNode(child, value);
      if (found) return found;
    }

    return null;
  }

  addNode(parentValue, childValue) {
    const parentNode = this.findNode(this.root, parentValue);
    if (parentNode) {
      const newChild = new TreeNode(childValue);
      parentNode.addChild(newChild);
    } else {
      alert(`Parent node '${parentValue}' not found.`);
    }
  }

  removeNode(value) {
    if (this.root && this.root.value === value) {
      alert("Cannot remove the root node.");
      return;
    }

    const parentNode = this.findParent(this.root, value);
    if (parentNode) {
      parentNode.removeChild(value);
    } else {
      alert(`Node '${value}' not found.`);
    }
  }

  findParent(currentNode, childValue) {
    if (!currentNode) return null;

    for (const child of currentNode.children) {
      if (child.value === childValue) return currentNode;
      const found = this.findParent(child, childValue);
      if (found) return found;
    }

    return null;
  }

  displayTree() {
    if (this.root) {
      return this.root.display();
    } else {
      return "Tree is empty.";
    }
  }
}

const tree = new InteractiveTree();

function performOperation() {
  const operation = document.getElementById("operation").value;
  const input1 = document.getElementById("input1").value.trim();
  const input2 = document.getElementById("input2").value.trim();

  if (operation === "setRoot") {
    tree.setRoot(input1);
  } else if (operation === "addNode") {
    tree.addNode(input1, input2);
  } else if (operation === "removeNode") {
    tree.removeNode(input1);
  }

  updateTreeDisplay();
}

function resetTree() {
  tree.root = null;
  updateTreeDisplay();
}

function updateTreeDisplay() {
  const treeDisplay = document.getElementById("tree");
  treeDisplay.textContent = tree.displayTree();
}

document.getElementById("operation").addEventListener("change", (event) => {
  const input2 = document.getElementById("input2");
  if (event.target.value === "addNode") {
    input2.style.display = "inline";
  } else {
    input2.style.display = "none";
  }
});
