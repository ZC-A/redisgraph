MATCH (n:Person {{id: '{}'}})-[:IS_LOCATED_IN]->(p:City)
RETURN
    n.id AS personid,
    n.firstName AS firstName,
    n.lastName AS lastName,
    n.birthday AS birthday,
    n.locationIP AS locationIP,
    n.browserUsed AS browserUsed,
    p.id AS cityId,
    n.gender AS gender,
    n.creationDate AS creationDate