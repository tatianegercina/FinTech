SELECT * FROM owners;

SELECT CONCAT(owners.first_name, ' ', owners.last_name) as owner_name, COUNT(estate_id) as estate_count
FROM owners
INNER JOIN estates_new ON owners.owner_id = estates_new.owner_id
INNER JOIN estate_type ON estates_new.estate_type_id = estate_type.estate_type_id
GROUP BY CONCAT(owners.first_name, ' ', owners.last_name);