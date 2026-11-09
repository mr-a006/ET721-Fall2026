console.log("Aqeel Hussain")
// collect items from the form
const itemForm = document.querySelector('#itemForm')

// add an event to the form
itemForm.addEventListener("submit", async function(event){
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value

    try{
        // await to pause request until the request finishes
        // fetch() sends an HTTP request to a server
        const res = await fetch("/items", {method: "POST", headers: {"Content-type": "application/json"},
            body: JSON.stringify({name: name, price: Number(price)})
        })
        const data = await res.json()

        document.querySelector('#response').innerText = "Item added successfully! ID: " + data.id
        itemForm.reset()
    }
    catch(error){
        document.querySelector('#response').innerText = "Error: " + error
    }
})

// LOADING ALL ITEMS
async function loaditems(){
    const res = await fetch("/items")
    const data = await res.json()

    // collect the elements to print all items
    const list = document.querySelector('.itemslist')

    // clear the list before loading items
    list.innerHTML = ""

    // use a loop to place each item in the json data to a list
    for (const id in data){
        const item = data[id]
        const li = document.createElement('li')

        li.textContent = `ID = ${id}, name = ${item.name}, price = $${item.price} `

        const updateButton = document.createElement('button')
        updateButton.textContent = "Update"
        updateButton.onclick = function(){
            showupdateform(id, item.name, item.price)
        }

        const deleteButton = document.createElement('button')
        deleteButton.textContent = "Delete"
        deleteButton.onclick = function(){
            deleteitem(id)
        }

        li.appendChild(updateButton)
        li.appendChild(deleteButton)
        list.appendChild(li)
    }

    if (Object.keys(data).length === 0){
        list.innerHTML = "<li>No items available.</li>"
    }
}

// function to collect the selected item
function showupdateform(id, name, price){
    document.querySelector("#updateSection").style.display = "block"
    document.querySelector("#updateName").value = name
    document.querySelector("#updateID").value = id
    document.querySelector("#updatePrice").value = price

    document.querySelector("#updateSection").scrollIntoView({behavior: "smooth"})
}

// function to update the selected item name and/or price
async function updateItem(){
    const id = document.querySelector("#updateID").value
    const name = document.querySelector("#updateName").value
    const price = document.querySelector("#updatePrice").value

    // update the json data in the localhost
    const res = await fetch(`/items/${id}`, {
        method: "PUT",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({name: name, price: Number(price)})
    })

    const html = await res.text()
    document.open()
    document.write(html)
    document.close()
}

// DELETE ITEM
async function deleteitem(id){
    const res = await fetch(`/items/${id}`, {
        method: "DELETE",
    })

    const html = await res.text()
    document.open()
    document.write(html)
    document.close()
}