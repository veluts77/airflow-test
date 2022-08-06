package org.acme

import javax.persistence.Column
import javax.persistence.GeneratedValue
import javax.persistence.Id
import javax.persistence.GenerationType
import javax.persistence.Entity
import javax.persistence.NamedQuery

@Entity(name="test_input")
class Input(
    @Column(nullable = false)
    val firstname: String = "",

    @Column(nullable = false)
    val lastname: String = "",

    @Column(nullable = false)
    val processed: Int = 0,

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int? = null
)