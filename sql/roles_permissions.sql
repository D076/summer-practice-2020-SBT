-- Roles
INSERT INTO role(id, name) VALUES (10, 'admin');
INSERT INTO role(id, name) VALUES (20, 'moderator');
INSERT INTO role(id, name) VALUES (30, 'super_user');
INSERT INTO role(id, name) VALUES (40, 'user');
INSERT INTO role(id, name) VALUES (50, 'guest');

-- Permissions
INSERT INTO permission(id, name) VALUES (60, 'read');
INSERT INTO permission(id, name) VALUES (50, 'rate');
INSERT INTO permission(id, name) VALUES (40, 'write');
INSERT INTO permission(id, name) VALUES (30, 'delete_post');
INSERT INTO permission(id, name) VALUES (20, 'edit_other_users_permissions');
INSERT INTO permission(id, name) VALUES (10, 'delete_collection');

-- Admin permissions
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 10);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 20);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 30);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 40);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 50);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (10, 60);

-- Moderator permissions
INSERT INTO roles_permissions(role_id, perm_id) VALUES (20, 20);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (20, 30);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (20, 40);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (20, 50);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (20, 60);

-- Superuser permissions
INSERT INTO roles_permissions(role_id, perm_id) VALUES (30, 40);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (30, 50);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (30, 60);

-- User permissions
INSERT INTO roles_permissions(role_id, perm_id) VALUES (40, 50);
INSERT INTO roles_permissions(role_id, perm_id) VALUES (40, 60);

-- Guest permissions
INSERT INTO roles_permissions(role_id, perm_id) VALUES (50, 60);