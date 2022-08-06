package org.acme

import javax.ws.rs.GET
import javax.ws.rs.POST
import javax.ws.rs.Path
import javax.ws.rs.Produces
import javax.ws.rs.core.MediaType

@Path("/error")
class ErrorResource {
    
    @POST
    fun addError(data: String) {
        println(data)
    }
}