
INSERT INTO family_children
(family, children)
VALUES
('Smith', 'Chris, Abby, Susy'),
('Jones', 'Steve, Mary, Dillion');

INSERT INTO first_normal_form
(family, children)
VALUES
('Smith', 'Abby'),
('Smith', 'Susy'),
('Jones', 'Mary'),
('Smith', 'Chris'),
('Jones', 'Dillion'),
('Jones', 'Mary');

INSERT INTO second_nf_family
(family_id, family)
VALUES
(1, 'Smith'),
(2, 'Jones');