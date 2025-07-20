class TrieNode {
    constructor () {
        this.children = {};
        this.count = 0;
        
    }
}

function insert(root, word) {
    let node = root;
    for(const char of word) {
        if (!node.children[char]) {
            node.children[char] = new TrieNode();
        }
        node = node.children[char]
        node.count++;
    }
}

function getCount(root, word) {
    let node = root;
    let inputCount = 0;
    
    for (const char of word) {
        inputCount++;
        node = node.children[char];
        if (node.count === 1) break;
    }
    return inputCount;
}

function solution(words) {
    const root = new TrieNode();
    for (const word of words) {
        insert(root, word);
    }
    return words.reduce((acc, word) => acc + getCount(root, word) , 0);
}