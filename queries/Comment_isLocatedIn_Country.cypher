MATCH (n:Comment {{id: '{}'}})-[:IS_LOCATED_IN]->(p:Country)
RETURN
    n.id AS commentid,
    p.id AS countryid
