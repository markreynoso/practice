// Algorithms


// Check if two strings are permutations of one another.
// Cracking the coding interview, page 73.
function permutations(str1, str2) {
  let str1_l = str1.split('')
  let str2_l = str2.split('')
  str1_l.sort()
  str2_l.sort()
  let one = str1_l.join('')
  let two = str2_l.join('')
  if (one === two) {
    return true
  } else {
    return false
  }
}
permutations('yes', 'yesm')



// Replace spaces with %20 and remove whitespace at the end.
function replace_the_space(string) {
  let end = string.trim()
  return end.replace(/\s/g, '%20')
}

replace_the_space('this is a test    ')




// Return letter and count of repeats unless longer than original.
function compressString(string) {
  let output = ''
  let count = 0
  let comp = string.charAt(0)
  for (let i = 0; i < string.length; i++) {
    if (string.charAt(i) === comp) {
      count++
      if (i === string.length - 1) {
        output += (comp + count)
      }
    } else {
      output += (comp + count)
      count = 1
      comp = string.charAt(i)
      if (i === string.length - 1) {
        output += (comp + count)
      }
    }
  }
  if (output.length < string.length) {
    return output
  } else {
    return string
  }
}
compressString('aabbbbcccc')



// Rotate matrix 90 degrees.
function rotateMatrix(matrix) {
  let newCoords = {}
  let y_con = matrix[0].length - 1
  for (let x = 0; x < matrix.length; x++) {
    for (let y = 0; y < matrix[0].length; y++) {
      newCoords[matrix[x][y]] = [y, y_con - x]
    }
  }
  Object.keys(newCoords).forEach(function(key) {
    let m1 = newCoords[key][0]
    let m2 = newCoords[key][1]
    matrix[m1][m2] = parseInt(key)
  })
  return matrix
}

rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])



// is s2 a substring of s1
function isSubstring(s1, s2) {
  if (s1.length !== s2.length) {
    return false
  }
  let f2l = s2
  for (let i = 0; i < s2.length; i++) {
    f2l = f2l.slice(1) + f2l[0]
    if (f2l === s1) {
      return true
    }
  }
  return false
}

isSubstring('waterbottle', 'erbottlewat')



// Untested - find LinkedList k to last node (recursion)
function kToLast(node, k, i){
  if (node === null) {
    return null
  }
  let next = node.next
  let output = kToLast(next, k, i)
  i++
  if (i === k) {
    return node
  }
  return output
}

// Partition a LinkedList at x value. Everything less than x and everything greater than x.
function partitionLL(ll, x) {
  let current = ll.head
  let previous = ll.head
  let divider = ll.head
  while (current) {
    if (current.data < x) {
      if (current === ll.head) {
        previous = current
        divider = current
        current = current.next
      } else {
        previous.next = current.next
        current.next = divider.next
        divider.next = current
        divider = current
        current = current.next
      }
    } else {
      previous = current
      current = current.next
    }
  }
  return ll
}
