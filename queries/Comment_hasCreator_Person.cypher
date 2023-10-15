MATCH (m:Comment {{id: '{}'}})-[:HAS_CREATOR]->(p:Person)
RETURN
    p.id AS personId,
    p.firstName AS firstName,
    p.lastName AS lastName