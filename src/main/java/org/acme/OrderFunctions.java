package org.acme;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class OrderFunctions {

    public JsonNode passThrough(JsonNode input) {
        return input == null ? null : ((ObjectNode) input.deepCopy());
    }
}
