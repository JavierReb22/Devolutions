function confirmarEliminacion(id){
    Swal.fire({
        title: '¿Desea Eliminar Este Usuario?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si',
        cancelButtonText: 'No'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            window.location.href='/eliminarcliente/'+id
          )
        }
      })
}



//Devolucion
function confirmarEliminacionDev(id){
  Swal.fire({
      title: '¿Desea Eliminar Esta devolucion?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si',
      cancelButtonText: 'No'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          window.location.href='/eliminarDev/'+id
        )
      }
    })
}


//Productos

function confirmarEliminacionProductos(id){
  Swal.fire({
      title: '¿Desea Eliminar Este Productos?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si',
      cancelButtonText: 'No'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          window.location.href='/eliminarproduct/'+id
        )
      }
    })
}