package org.acme

import javax.inject.Inject
import javax.persistence.EntityManager
import javax.ws.rs.GET
import javax.ws.rs.Path
import javax.ws.rs.Produces
import javax.ws.rs.core.MediaType
import javax.ws.rs.POST
import javax.ws.rs.DELETE
import javax.ws.rs.PUT
import org.jboss.resteasy.reactive.RestQuery
import kotlin.collections.mutableListOf

@Path("/input")
class InputResource {

    @Inject
    lateinit var repo: InputRepository

    @POST
    @Produces(MediaType.TEXT_PLAIN)
    fun postInput(@RestQuery firstname: String, @RestQuery lastname: String): String {
        repo.save(Input(firstname, lastname))
        return "Written to DB: ${firstname} ${lastname}"
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    fun getAllInputs() = repo.findAll().toList()

    @DELETE
    fun deleteAll() = repo.deleteAll()

    @PUT
    @Produces(MediaType.TEXT_PLAIN)
    fun resetAll() {
        val all = repo.findAll().toMutableList()
        all.forEach { println("${it.id} ${it.processed}") }
        val newList = all.map { Input(firstname = it.firstname, lastname = it.lastname, id = it.id, processed = 0) }
        newList.forEach { println("${it.id} ${it.processed}") }
        repo.saveAll(newList)
    }
}
