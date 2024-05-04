SELECT E1.ID, E1.GENOTYPE, E2.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS E1
LEFT JOIN ECOLI_DATA AS E2
    ON E1.PARENT_ID = E2.ID
WHERE (E1.GENOTYPE & E2.GENOTYPE) = E2.GENOTYPE
ORDER BY E1.ID;
